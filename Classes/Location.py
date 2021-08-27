#!/usr/bin/env python
#coding: utf-8
'''
Created on 27-ago-2021

@author: 109733
'''

'''
ITS FOR A HEX MAP, SO IT MUST BE SOMETHING LIKE

    -4,2    -2,2    0,2    2,2    4,2
-5,1    -3,1    -1,1    1,1    3,1    
    -4,0    -2,0    0,0    2,0    4,0   #Debajo de aqui, el segundo digito serían negativos 
-5,1    -3,1    -1,1    1,1,    3,1
    -4,2    -2,2    0,2    2,2    4,2
    
CONCLUSION, LAS COORDENADAS TIENEN QUE SER O AMBAS IMPARES O AMBAS PARES
'''
import traceback
from random import randint

class Location:
    
    def __init__(self, name, coordinates, landType, **kwargs):
        self._landTypes = ['Plain', 'Mountain', 'Sea', 'Forest']
        self._locationData = {}
        self._createLocation(name, coordinates, landType, **kwargs)
        
    def _checkCoordinates(self, coordinate_tuple):
        x = coordinate_tuple[0]
        y = coordinate_tuple[1]
        
        if not (type(x) == int and type(y)==int):
            return False
        
        return (y%2 != 0) == (x%2 != 0)
    
    def _checkLandType(self, lT):
        val = lT.capitalize()
        return val in self._landTypes
    
    
    def _createLocation(self, name, coordinates, landType, **kwargs):
        result = {'RESULT':False}
        try:
            dicData = {}
            dicData['name'] = name
            if not self._checkCoordinates(coordinates):
                raise(Exception('Both int of the coordinates of the location must be even or odd'))
            dicData['coordinates'] = coordinates
            
            if not self._checkLandType(landType):
                raise(Exception("'landType' attribute must be one of the folowing: "+", ".join(self._landTypes)))
            dicData['landType'] = landType
            
            dicData['CanBuildIn'] = dicData['landType'] not in ['Sea']
            
            for key, value in kwargs.items():
                dicData[key] = value
            
            self._locationData = dicData
            result['RESULT'] = True
            
        except Exception as e:
            result['ERROR'] = f'An error ocurred creating the location. {e}'
            result['LOCATION'] = f'{traceback.format_exc()}'
            
        return result
    
    def getAttr(self, attr):
        if attr not in list(self._cityData.keys()):
            raise (Exception(f"Location Class has no '{attr}' atributte"))
        return self._cityData[attr]
    
    def setAttr(self, attr, value):
        if attr not in list(self._cityData.keys()):
            raise (Exception(f"Location Class has no '{attr}' atributte"))
        attrType = self._cityData[attr].__class__
        if attrType != type(value):
            raise (Exception(f"The '{attr}' atributte value must be type {attrType.__name__}"))
        
        self._cityData[attr] = value
    
    def __str__(self):
        for key in list(self._locationData.keys()):
            globals()[key] = self._locationData[key]
            
        format = f'The terrain knows as {name} is a {landType} and is located in the ({coordinates[0]},{coordinates[1]}) coordinates.'
        return format
        
        
l = Location('Broken Limbs', (3,7), 'Mountain')
print(l)