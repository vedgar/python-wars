import random



class Space(object):
	pass

class Ship(object):
	def __init__(self):
		self.dtype = 'Ship'
		self.shields = 0
		self.max_shields = 0
		self.alive = True
		self.title = ''
		
		
	def take_damage(self, damage):
		self.shields -= damage
		if self.shields < 1:
			print self.title, 'Destroyed!!!'
			self.alive = False
			return self.alive
		print self.title + ' shields down to ' + str(self.shields) + ' of ' + str(self.max_shields) + '.'
		return self.alive
	
class Component(object):
	def __init__(self):
		self.dtype = 'Component'
	def action(self):
		pass		
	
class Spinal_Mount(Component):
	def __init__(self):
		self.av = 0
		self.dv = 0				
		self.volume = 1
		self.capacitor = 100
		self.max_capacitor = 100		
		self.recharge_capacitor = 10			
		self.range = 15
		self.option = 'Fire (S)pinal Mount'
		
	def recharge(self):
		self.capacitor = min(self.max_capacitor, self.capacitor + self.recharge_capacitor)		
		
	def action(self,me=None,enemy=None):
		print 'Firing Spinal Mount!'
		hit = False
		energy = 0
		survived = True
		for laser in range(10):
			energy = (laser + 1) ** 2	
			if energy > self.capacitor:
				print 'Spinal Mount out of juice'
				break
			if not hit:
				av = random.randrange(me.av + self.av + laser)
				dv = random.randrange(enemy.dv)
				if av > dv:
					hit = True
				else:
					print 'Spinal Mount missed'
			if hit:
				print 'Spinal Mount locked on'
				survived = enemy.take_damage(10)
			if not survived:
				break

		self.capacitor -= energy
		print 'Spinal mount firing sequence over.'		
		print 'Spinal mount capacitor at ',self.capacitor
		return survived

	
class Pulsar(Component):
	def __init__(self):
		self.av = 0
		self.dv = 0			
		self.volume = 1
		self.range = 5
		self.option = 'Fire (P)ulsar'		
		
	def action(self,me=None,enemy=None):
		print self.title + ' firing Pulsar!'
		av = random.randrange(me.av + self.av)
		dv = random.randrange(enemy.dv)		
		return enemy.take_damage(10)
		

class Missile(Component):
	def __init__(self):
		self.av = 20
		self.dv = 0		
		self.damage = 'd2'
		self.volume = 1
		self.range = 10
		self.ammo = 5
		self.option = 'Fire (M)issile'			
		
	def action(self,me=None,enemy=None):
		if self.ammo == 0:
			print 'Out of missiles.'
			return True
		print 'Launching missile!'
		self.ammo -= 1
		av = random.randrange(me.av + self.av)
		dv = random.randrange(enemy.dv)		
		if av < dv:
			print 'Missile missed'		
			return True
		damage = (random.randrange(10) + 1) * (random.randrange(10) + 1)
		return enemy.take_damage(damage)		
		
class ECM(Component):
	def __init__(self):
		self.av = 0
		self.dv = 40
		self.volume = 1
		self.option = '(E)CM'
		
	def action(self,me=None,enemy=None):
		return True

class Frigate(Ship):
	def __init__(self,name='',id=''):
		Ship.__init__(self)
		self.title = name
		self.id = id
		self.av = 40
		self.dv = 1 + (random.randrange(10) * random.randrange(10))
		self.volume = 2
		self.shields = 30
		self.max_shields = 30
		self.recharge_shields = 3
		self.thrust = 8
		self.pulsar = Pulsar()
		self.ecm = ECM()			
		self.side = 'bad'

class Cruiser(Ship):
	def __init__(self,name='',id=''):
		self.title = name	
		self.id = id
		self.av = 20
		self.dv = 10
		self.volume = 3
		self.shields = 100
		self.max_shields = 100
		self.recharge_shields = 1
		self.thrust = 5
		self.spinal_mount = Spinal_Mount()
		self.missile = Missile()
		self.ecm = ECM()
		self.side = 'good'		
		
		