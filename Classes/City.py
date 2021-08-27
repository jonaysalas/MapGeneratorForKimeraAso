#!/usr/bin/env python
#coding: utf-8
'''
Created on 27-ago-2021
@author: 109733
'''

from random import randint
import traceback


class City:
    def __init__(self, name, location, population={}, **kwargs):
        self._cityData = {}
        self._createCity(name, location, population, **kwargs)
        
    def _revisePopulation(self, pop_dict):
        dict_copy = pop_dict
        totalPercent = sum(list(dict_copy.values()))
        if totalPercent > 100:
            prov_percent = 0
            for key in list(dict_copy.keys()):
                dict_copy[key] = dict_copy[key]*100//totalPercent
                prov_percent += dict_copy[key]
            totalPercent = prov_percent
        
        if totalPercent < 100:
            if 'Others' in list(dict_copy.keys()):
                dict_copy['Others'] = dict_copy['Others'] + (100-totalPercent)
            elif 'Otros' in list(dict_copy.keys()):
                dict_copy['Others'] = dict_copy['Otros'] + (100-totalPercent)
                del dict_copy['Otros']
            else:
                dict_copy['Others'] = 100-totalPercent
            totalPercent = 100
                    
        #All races with 0% are cleanes (moved to others)
        for key in list(dict_copy.keys()):
            if dict_copy[key] == 0:
                del dict_copy[key]
        
        pop_dict = dict_copy
        del dict_copy
        
        return pop_dict
                
    def _randomPopulation(self, **kwargs):
        '''
        **kwars must follow the next format:
        Race_name = percentage
        '''
        pre_dict = {}
        totalPercent = 0 #In case totalpercent is greater than 100, we will calculate the percentage according to this value.
        for race, percent in kwargs.items():
            pre_dict[race.capitalize()] = percent
            totalPercent += percent
        
        if totalPercent < 95:
            for race in ['Humans', 'High Elves', 'Dwarfs', 'Tieflings', 'Halflings', 'Orcs', 'Wood Elves']:
                if race in list(pre_dict.keys()) : continue
                pre_dict[race] = randint(0, 100-totalPercent)
                totalPercent += pre_dict[race]
                if totalPercent >= 95:
                    break
        dict = self._revisePopulation(pre_dict)
        
        return dict
    
    def _createCity(self, name, location, population={}, **kwargs):
        result = {'RESULT':False}
        try:
            dicData = {}
            dicData['name'] = name
            dicData['location'] = location
            if population == {}:
                population = self._randomPopulation(**kwargs)
            else:
                population = self._revisePopulation(population)
            dicData['population'] = population
            
            self._cityData = dicData
            result['RESULT'] = True
            
        except Exception as e:
            result['ERROR'] = f'An error ocurred creating the city. {e}'
            result['LOCATION'] = f'{traceback.format_exc()}'
            
        return result
    
    def getAttr(self, attr):
        if attr not in list(self._cityData.keys()):
            raise (Exception(f"City Class has no '{attr}' atributte"))
        return self._cityData[attr]
    
    def setAttr(self, attr, value):
        if attr not in list(self._cityData.keys()):
            raise (Exception(f"City Class has no '{attr}' atributte"))
        attrType = self._cityData[attr].__class__
        if attrType != type(value):
            raise (Exception(f"The '{attr}' atributte value must be type {attrType.__name__}"))
        
        self._cityData[attr] = value
    
    def __str__(self):
        for key in list(self._cityData.keys()):
            globals()[key] = self._cityData[key]
            
        format = f'The city {name} is located on {location}. These are its population percentages:\n'
        popu = [f'{race}: {population[race]}%' for race in list(population.keys())]
        format += '\n'.join(popu)
        
        return format