from collections.abc import Callable
import math
import os
import unittest
import turtle

class Vector(Callable):
    PRECISION=6
    __slots__ = ('_x','_y','_hash')
    def __init__(self,x,y):
        self._hash= None
        self._x= x
        self._y= y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, val):
        if self._hash is not None:
            raise ValueError('Cannot set x after hashing')
        self._x= val

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, val):
        if self._hash is not None:
            raise ValueError('Cannot set y after hashing')
        self._y= val

    def __hash__(self):
        if self._hash is None:
            pair= (self.x, self.y)
            self._hash= hash(pair)
        return self._hash

    def __getitem__(self, index):
        if index==0:
            return self.x
        elif index==1:
            return self.y
        else:
            raise ValueError('Index out of range')

    def __len__(self):
        return 2

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x== other.x and self.y== other.y
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Vector):
            return self.x!= other.x or self.y!= other.y
        else:
            return NotImplemented

    def copy(self):
        type_self= type(self)
        return type_self(self.x, self.y)

    def __add__(self, other):
        if self._hash is not None:
            return ValueError('Already hash value set, cannot change vector')
        self_copy= self.copy()
        if isinstance(other, Vector):
            self_copy.x += other.x
            self_copy.y += other.y
        else:
            self_copy.x += other
            self_copy.y += other
        return self_copy

    def __sub__(self, other):
        if self._hash is not None:
            return ValueError('Already hash value set, cannot change vector')
        self_copy= self.copy()
        if isinstance(other, Vector):
            print('Inside')
            self_copy.x -= other.x
            self_copy.y -= other.y
        else:
            self_copy.x -= other
            self_copy.y -= other
        return self_copy

    def __mul__(self, other):
        if self._hash is not None:
            return ValueError('Already hash value set, cannot change vector')
        self_copy= self.copy()
        if isinstance(other, Vector):
            self_copy.x= self_copy.x * other.x
            self_copy.y= self_copy.y * other.y
        else:
            self_copy.x = self_copy.x * other
            self_copy.y = self_copy.y * other
        return self_copy

    def __truediv__(self, other):
        if self._hash is not None:
            return ValueError('Already hash value set, cannot change vector')
        self_copy= self.copy()
        if isinstance(other, Vector):
            self_copy.x = self_copy.x / other.x
            self_copy.y = self_copy.y / other.y
        else:
            self_copy.x = self_copy.x / other
            self_copy.y = self_copy.y / other
        return self_copy

    def move(self, other):
        return self.__add__(other)

    def scale(self, other):
        return self.__mul__(other)

    def __neg__(self):
        copy_self= self.copy()
        copy_self.x = -copy_self.x
        copy_self.y = -copy_self.y
        return copy_self

    def __abs__(self):
        return (self.x**2 + self.y**2) ** .5

    def __str__(self):
        name= type(self).__name__
        return '{}({},{})'.format(name,self.x,self.y)

    def __call__(self):
        pass

# vect= Vector(1,2)
# print(vect.__slots__)
# print(vect.x)
# print(vect[1])
# print(len(vect))
# # vect.x=10
# print(vect.x)
# vect.x=20
# print(vect.x)
# hash_val= hash(vect)
# print(hash_val)
# vect.x=30
# print(vect.x)
# print(vect==vect)
#
# vect2= Vector(1,2)
# print(vect==vect2)
# print(vect!=vect2)
# vect3= Vector(2,4)
# print(vect==vect3)
# print(vect!=vect3)
#
# type_vect= type(vect)
# print(type_vect)
# vect4= type_vect(1,2)
# print(id(vect4),id(vect))
# print(vect4==vect)
#
# new_sum= vect+vect3
# print('new x= {} and y= {}'.format(new_sum[0],new_sum[1]))
# sub_result= vect-vect3
# print('new x= {} and y= {}'.format(sub_result[0],sub_result[1]))
#
# d= vect.move(vect3)
# print(d[0],d[1])
#
# d=-vect
# print(d[0],d[1])

# print(abs(vect))
# print(d)