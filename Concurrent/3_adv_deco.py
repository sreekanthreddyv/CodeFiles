import datetime
import time


# Basic Decorator
def time_this(func):
	def new_function(*a, **kw):
		before = datetime.datetime.now()
		x = func(*a, **kw)
		after = datetime.datetime.now()
		print(f"Elapsed time: {after - before}")
		return x

	return new_function


@time_this
def hacker(num):
	time.sleep(3)
	print("finished")


# Decorator with Parameters
# To do this we need a function that returns a decorator:
def requires_permission(sPermission):
	def decorator(func):
		def decorated(*a, **kw):
			lPermission = ['administrator', 'logged_in', 'premium_member']  # requires_permission
			if sPermission in lPermission:
				return func(*a, **kw)
			raise Exception("Permission Denied")

		return decorated

	return decorator


@requires_permission('administrator')
def delete_user(iUserid):
	print(iUserid)
	return ['logged_in']


@requires_permission('premium_member')
def premium_checkpoint():
	print("save the game progress, only accessable to premium members")


# Here is the general form of a decorator with arguments and an illustration of it's use:
def outer_decorator(*outer_args, **outer_kargs):
	def decorator(func):
		def decorated(*args, **kw):
			# do_something(*outer_args, **outer_kargs)
			return func(*args, **kw)

		return decorated

	return decorator


@outer_decorator(1, 2, 3)
def foo(a, b, c):
	print(a, b, c)


# Decorating Classes
# Firstly, we know it needs to take in a class as an argument, and return a class.
def time_all_class_methods(Cls):
	class NewCls:git

		def __init__(self, *args, **kwargs):
			self.oInstance = Cls(*args, **kwargs)

		def __getattribute__(self, item):
			"""
			this is called whenever any attribute of a NewCls object is accessed. This function first tries to
			get the attribute off NewCls. If it fails then it tries to fetch the attribute from self.oInstance (an
			instance of the decorated class). If it manages to fetch the attribute from self.oInstance, and
			the attribute is an instance method then `time_this` is applied.
			"""
			try:
				x = super(NewCls, self).__getattribute__(item)
			except AttributeError:
				pass
			else:
				return x
			x = self.oInstance.__getattribute__(item)
			if type(self.__init__) == type(x):  # it is an instance method
				return time_this(x)  # this is equivalent of just decorating the method with time_this
			else:
				return x
	return NewCls


@time_all_class_methods
class Foo:
	def a(self):
		print("entering a")
		import time
		time.sleep(3)
		print("exiting a")


if __name__ == "__main__":
	# hacker(25)
	# delete_user(34)
	# premium_checkpoint()
	oF = Foo()
	oF.a()
