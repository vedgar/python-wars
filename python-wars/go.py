import stuff
import random
import md5
import sys


enemies = 'arrogance,killer,demon,evil,slaughter,monster,couch,tempest,bunny'.split(',')

name = 'Pythonista'
while True:
	zargons = raw_input('How many Zargons can you handle (1-9)? ')
	try:
		zargons = int(zargons)
	except:
		print 'Use numbers!  No special characters or letters or stuff!'
		continue
	if zargons < 1 or zargons > 9:
		print 'Thats not between 1 and 9 Zargons!'
		continue
		
	break

space = stuff.Space()
space.me = stuff.Cruiser(name)
count = 0
for enemy in range(zargons):
	title = enemies[count].capitalize()
	id = md5.new(title + str(count)).hexdigest()
	setattr(space,id,stuff.Frigate(title,id,count * 10))
	count += 1
	

turn = 0
while True:



	print '*' * 80
	print 'Turn',turn + 1
	print '*' * 80
	
	#list enemies
	print 'Enemies       Shields  Defense'
	ships = space.__dict__.keys()

	ships.sort()
	short_names = {}
	win = True
	hero = True
	for ship in ships:
		ship = getattr(space, ship)
		if ship.side == 'good': continue
		win = False
		short_names[ship.title[0].lower()] = ship
		ship.recharge()
		name = '(' + ship.title[0] + ')' + ship.title[1:]
		if ship.shields == 30:
			remaining = str(100)
		else:
			remaining = str((ship.shields / ship.max_shields) * 100)[:2]
		pad = ''
		for i in range(12-len(name)): pad += ' '
		print '%s %s  %s%% -    %s' % (name,pad,remaining,ship.dv)

		if turn:
			action = random.randrange(2)
			if action == 0:
				hero = ship.pulsar.action(ship,space.me)
				if not hero:
					print 'SHIP DESTROYED!!!'			
					print 'You lose!!!'
					print 'You lose!!!'
					print 'You lose!!!'
					sys.exit()		
				
			else:
				print '	%s coming about for optimal firing position' % ship.title
				ship.recharge()


		

	if win:
		print 'You win!!!'
		print 'You win!!!'
		print 'You win!!!'
		sys.exit()		


	#list my ship	

	for i in range(2): print '='*80	
	print 'The Good Ship', space.me.title
	print 'Shields:', space.me.shields

	target = raw_input('Who is your target? ').lower()
	target = short_names[target]
	print 'Target:',target.title
	print 'Fire (S)pinal Mount - Capacitor at %s %%' % space.me.spinal_mount.capacitor
	if space.me.missile.ammo:
		print 'Fire (M)issle - %s missiles remaining' % space.me.missile.ammo			
	
	action = raw_input('What is your action? ').lower()
	if action == 's':
		print 'Spinal Mount', target.title
		survived = space.me.spinal_mount.action(space.me,target)
		if not survived:
			delattr(space,target.id)
	elif action == 'm' and space.me.missile.ammo:
		print 'Missile', target.title
		survived = space.me.missile.action(space.me,target)
		if not survived:
			delattr(space,target.id)		
		
	space.me.recharge()
	turn += 1		