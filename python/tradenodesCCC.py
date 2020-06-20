import shutil
import re
import random
import codecs

def start2():
    raw = '1301_tradenodes.txt'
    filename = '0TN2.txt'
    newFName = '0TN3.txt'
    shutil.copyfile(raw, filename)
    file = open(filename, 'r+')
    fileIterator = enumerate(file)
    array = []
    counter = -1
    counter2 = 2
    counter3 = 3004
    toplevel = re.compile('^\\w+')
    outgoing = re.compile('outgoing')
    members = re.compile('members')
    cbracket = re.compile('^((?!\\}).)*$')
    name = re.compile('\"\\w+')
    
    with open(newFName, 'w') as output: 
        for i, line in fileIterator:
            if re.search(outgoing, line) == None:
                output.write(line)
                
            for match in re.finditer(toplevel, line):
                nArray = []
                nArray.append(match.group())#.replace('_',''))
                array.append(nArray)
                counter += 1
                counter2 = 2
                
                array[counter].append(str(counter3))
                counter3 += 1
                
                rr = random.randint(0, 255)
                bb = random.randint(0, 255)
                gg = random.randint(0, 255)
                array[counter].append('color = { '+str(rr)+' '+str(bb)+' '+str(gg)+' }')
                
            if re.search(members, line) != None:
                array[counter].append(next(fileIterator)[1])
                line2 = next(fileIterator)[1]
                while re.search(cbracket, line2):
                    array[counter].append(line2)
                    line2 = next(fileIterator)[1]
        
    print(array)
    definition(array)
    
def definition(array):
    filename = '1301_definition.csv'
    newFName = 'definition.csv'
    toplevel = re.compile('.*\\;')
    
    file = open(filename, 'r+')
    
    with open(newFName, 'w') as output:
        for line in file:
            try:
                four = int(line[0:4])
                if four >= int(array[0][1]) and four <= int(array[-1][1]):
                    for match in re.finditer(toplevel, line):
                        output.write(match.group()+'CN'+array[four-int(array[0][1])][0]+';x\n')
                else:
                    output.write(line)
            except:
                output.write(line)
    provincegroup(array)
                
def provincegroup(array):
    newFName = 'provincegroup.txt'
    
    raw = '1301_colonial_regions.txt'
    filename = '0TN4.txt'
    newFFName = '0TN5.txt'
    shutil.copyfile(raw, filename)
    file = open(filename, 'r+')
    fileIterator = enumerate(file)
    array2 = []
    counter = -1
    counter2 = 2
    counter3 = 3004
    toplevel = re.compile('^\\w+')
    outgoing = re.compile('outgoing')
    members = re.compile('provinces')
    cbracket = re.compile('^((?!\\}).)*$')
    name = re.compile('\"\\w+')
    
    with open(newFFName, 'w') as output: 
        for i, line in fileIterator:
            if re.search(outgoing, line) == None:
                output.write(line)
                
            for match in re.finditer(toplevel, line):
                nArray = []
                nArray.append(match.group())
                array2.append(nArray)
                counter += 1
                counter2 = 2
                
                #array[counter].append(str(counter3))
                counter3 += 1
                
                rr = random.randint(0, 255)
                bb = random.randint(0, 255)
                gg = random.randint(0, 255)
                #array[counter].append('color = { '+str(rr)+' '+str(bb)+' '+str(gg)+' }')
                
            if re.search(members, line) != None:
                array2[counter].append(next(fileIterator)[1])
                line2 = next(fileIterator)[1]
                while re.search(cbracket, line2):
                    array2[counter].append(line2)
                    line2 = next(fileIterator)[1]
                    
    print(array2)
    
    raw = '1301_trade_companies.txt'
    filename = '0TN6.txt'
    newFFName = '0TN7.txt'
    shutil.copyfile(raw, filename)
    file = open(filename, 'r+')
    fileIterator = enumerate(file)
    array3 = []
    counter = -1
    counter2 = 2
    counter3 = 3004
    toplevel = re.compile('^\\w+')
    outgoing = re.compile('outgoing')
    members = re.compile('provinces')
    cbracket = re.compile('^((?!\\}).)*$')
    name = re.compile('\"\\w+')
    
    with open(newFFName, 'w') as output: 
        for i, line in fileIterator:
            if re.search(outgoing, line) == None:
                output.write(line)
                
            for match in re.finditer(toplevel, line):
                nArray = []
                nArray.append(match.group())
                array3.append(nArray)
                counter += 1
                counter2 = 2
                
                #array[counter].append(str(counter3))
                counter3 += 1
                
                rr = random.randint(0, 255)
                bb = random.randint(0, 255)
                gg = random.randint(0, 255)
                #array[counter].append('color = { '+str(rr)+' '+str(bb)+' '+str(gg)+' }')
                
            if re.search(members, line) != None:
                array3[counter].append(next(fileIterator)[1])
                line2 = next(fileIterator)[1]
                while re.search(cbracket, line2):
                    array3[counter].append(line2)
                    line2 = next(fileIterator)[1]
                    
    print(array3)
    
    with open(newFName, 'w') as output:
        output.write('colonialdumb_region = {\n\t')
        for i in range(0,len(array)):
            output.write(array[i][1]+' ')
        output.write('\n}\n\n')
        for i in range(0,len(array)):
            output.write('colonial_'+array[i][0]+'_region = {\n')
            for j in range(3,len(array[i])):
                output.write(array[i][j][1:])
            output.write('}\n\n')
        for i in range(0,len(array2)):
            output.write(array2[i][0]+' = {\n')
            for j in range(1,len(array2[i])):
                output.write(array2[i][j][1:])
            output.write('}\n\n')
        for i in range(0,len(array3)):
            output.write(array3[i][0]+' = {\n')
            for j in range(1,len(array3[i])):
                output.write(array3[i][j][1:])
            output.write('}\n\n')
    trade_companies(array)

def trade_companies(array):
    newFName = '00_trade_companies.txt'
    
    with open(newFName, 'w') as output:
        for i in range(0,len(array)):
            output.write('trade_company_tc'+array[i][0]+' = {\n')
            output.write('\t'+array[i][2]+'\n\n')
            output.write('\tprovinces = {\n')
            for j in range(3,len(array[i])):
                output.write(array[i][j])
            output.write('\t}\n\n')
            output.write('\tnames = {\n')
            output.write('\t\tname = \"TRADE_COMPANY_'+array[i][0].upper()+'_Root_Culture_GetName\"\n')
            output.write('\t}\n')
            output.write('\tnames = {\n')
            output.write('\t\tname = \"TRADE_COMPANY_'+array[i][0].upper()+'_Trade_Company\"\n')
            output.write('\t}\n')
            output.write('')
            output.write('}\n')
    colonial_regions(array)
            
def colonial_regions(array):
    newFName = '00_colonial_regions.txt'
    
    with open(newFName, 'w') as output:
        for i in range(0,len(array)):
            output.write('colonial_cn'+array[i][0]+' = {\n')
            output.write('\t'+array[i][2]+'\n\n')
            output.write('\tprovinces = {\n')
            output.write('\t\t'+array[i][1]+'\n')
            output.write('\t}\n\n')
            output.write('\tnames = {\n')
            output.write('\t\tname = \"COLONIAL_'+array[i][0].upper()+'_Root_Culture_GetName_'+array[i][0].capitalize()+'\"\n')
            output.write('\t}\n')
            output.write('\tnames = {\n')
            output.write('\t\tname = \"COLONIAL_REGION_New_Root_GetName\"\n')
            output.write('\t}\n')
            output.write('}\n')                            
    FlavorCN(array)
            
def FlavorCN(array):
    newFName = 'FlavorCN.txt'
    
    with open(newFName, 'w') as output:
        output.write('namespace = flavor_cn\n')
        for i in range(0,len(array)):
            prov = array[i][1]
            name = array[i][0]
            eventtext = '''
country_event = {
    id = flavor_cn.'''+prov+'''
    title = "flavor_cn.'''+prov+'''"
    desc = "flavor_cn.DESC"
    picture = EXPLORERS_eventPicture
    is_triggered_only = yes
    
    option = {
        name = "flavor_cn.option1"
        ai_chance = {
            factor = 999
            modifier = {
                factor = 0
                NOT = { has_global_flag = all_ai_colonial }
                OR = {
                    has_global_flag = no_ai_colonial
                    any_owned_province = {
                        NOT = { province_group = colonial_'''+name+'''_region }
                        is_colony = no
                        colonial_'''+name+'''_region = {
                            owned_by = ROOT
                            is_colony = no
                            NOT = {
                                province_distance = {
                                    who = PREV
                                    distance = 231
                                }
                            }
                        }
                    }
                }
            }
        }
        custom_tooltip = cn_toopltip_option1
        hidden_effect = {
            '''+prov+''' = {
                 cede_province = ROOT
                 add_core = ROOT
            }
        }
    }
    
    option = {
        name = "flavor_cn.option2"
        ai_chance = {
            factor = 1
            modifier = {
                factor = 0
                NOT = { has_global_flag = no_ai_colonial }
                OR = {
                    has_global_flag = all_ai_colonial
                    NOT = {
                        any_owned_province = {
                            NOT = { province_group = colonial_'''+name+'''_region }
                            is_colony = no
                            colonial_'''+name+'''_region = {
                                owned_by = ROOT
                                is_colony = no
                                NOT = {
                                    province_distance = {
                                        who = PREV
                                        distance = 231
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        custom_tooltip = cn_toopltip_option2
        hidden_effect = {
            set_country_flag = tc_'''+name+'''
            '''+prov+''' = { clr_province_flag = iscity }
        }
    }
}
    '''
            output.write(eventtext)
    FlavorCNNat(array)
    
def FlavorCNNat(array):
    newFName = 'FlavorCNNat.txt'
    
    with open(newFName, 'w') as output:
        output.write('namespace = flavor_cnnat\n')
        for i in range(0,len(array)):
            prov = array[i][1]
            name = array[i][0]
            eventtext = '''
country_event = {
    id = flavor_cnnat.'''+prov+'''0
    title = "flavor_cnnat.1t"
    desc = "flavor_cnnat.1d"
    picture = EXPLORERS_eventPicture
    hidden = yes
    
    trigger = {
        NOT = { has_country_flag = tc_'''+name+''' }
        '''+prov+''' = {
            NOT = { has_province_flag = iscity }
        }
        is_colonial_nation = no
        calc_true_if = {
            any_core_province = {
                province_group = colonial_'''+name+'''_region
                owned_by = ROOT
                is_overseas = yes
            }
            amount = 1
        }
    }
    
    immediate = {
        '''+prov+''' = { set_province_flag = iscity }
        save_global_event_target_as = cn_'''+name+'''
        every_subject_country = {
            limit = {
                event_target:cn_'''+name+''' = {
                    tag = ROOT
                }
                capital_scope = {
                    province_group = colonial_'''+name+'''_region
                }
            }
            clear_global_event_target = cn_'''+name+'''
            save_global_event_target_as = cn_'''+name+'''
        }
        
        if = {
            limit = {
                event_target:cn_'''+name+''' = {
                    tag = ROOT
                }
            }
            clear_global_event_target = cn_'''+name+'''
            country_event  = {
                id = flavor_cn.'''+prov+'''
            }
        }
        else = {
            '''+prov+''' = { clr_province_flag = iscity }
            event_target:cn_'''+name+''' = {
                country_event  = {
                    id = flavor_cnnat.'''+prov+'''2
                }
            }
            clear_global_event_target = cn_'''+name+'''
        }
    }
    
    option = {
        #hidden
    }
}

country_event = {
    id = flavor_cnnat.'''+prov+'''1
    title = "flavor_cnnat.1t"
    desc = "flavor_cnnat.1d"
    picture = CONQUEST_eventPicture
    hidden = yes
    
    trigger = {
        is_colonial_nation = yes
        owns = '''+prov+'''
    }
    
    immediate = {
        hidden_effect = {
            colonial_parent = {
                every_owned_province = {
                    limit = {
                        AND = {
                            province_group = colonial_'''+name+'''_region
                            is_city = yes 
                            is_overseas = yes
                        }
                    }
                    remove_core = owner
                    add_core = ROOT
                    cede_province = ROOT
                }
                PREV = {
                    change_primary_culture = PREV
                    change_religion = PREV
                }
            }
        }
    }
    option = {
        name = "flavor_cnnat.1a"
        hidden_effect = {
            add_treasury = 100
            every_owned_province = {
                limit = { 
                    AND = { 
                        owned_by = ROOT
                        province_group = colonialdumb_region
                    }
                }
                remove_core = ROOT
                cede_province = XXX
                clr_province_flag = iscity
            }
        }
        random_owned_province = {
            limit = {
                controlled_by = ROOT
            }
            infantry = ROOT
        }
    }
}

country_event = {
    id = flavor_cnnat.'''+prov+'''2
    title = "flavor_cnnat.2t"
    desc = "flavor_cnnat.2d"
    picture = CONQUEST_eventPicture
    is_triggered_only = yes
    hidden = yes
    
    immediate = {
        hidden_effect = {
            colonial_parent = {
                every_core_province = {
                    limit = {
                        AND = {
                            province_group = colonial_'''+name+'''_region
                            is_city = yes 
                            is_overseas = yes
                        }   
                    }
                    remove_core = owner
                    add_core = ROOT
                    cede_province = ROOT
                }
                every_owned_province = {
                    limit = {
                        AND = {
                            province_group = colonial_'''+name+'''_region
                            is_city = yes 
                            is_overseas = yes
                        }
                    }
                    cede_province = ROOT
                }
            }
        }
    }
    
    option = {
        #hidden
    }
}

    '''
            output.write(eventtext)
    area(array)
    
def area(array):
    filename = '1301_area.txt'
    newFName = 'area.txt'
    
    file = open(filename, 'r+')
    
    with open(newFName, 'w') as output:
        for line in file:
            if line == '#No restriction on size.\n':
                output.write(line)
                output.write('\ncolonialdumb_region = {\n\t')
                for i in range(0,len(array)):
                    output.write(array[i][1]+' ')
                output.write('\n}\n')
            else:
                output.write(line)
    climate(array)
                
def climate(array):
    filename = '1301_climate.txt'
    newFName = 'climate.txt'
    
    file = open(filename, 'r+')
    
    with open(newFName, 'w') as output:
        for line in file:
            if line == 'tropical = {\n':
                output.write(line)
                output.write('\t#CN\n\t')
                for i in range(0,len(array)):
                    output.write(array[i][1]+' ')
                output.write('\n')
            else:
                output.write(line)
    continent(array)
                
def continent(array):
    filename = '1301_continent.txt'
    newFName = 'continent.txt'
    
    file = open(filename, 'r+')
    
    with open(newFName, 'w') as output:
        output.write('colonialdumb_region = {\n\t')
        for i in range(0,len(array)):
            output.write(array[i][1]+' ')
        output.write('\n}\n\n')
        for line in file:
            output.write(line)
    defaultmap(array)
            
def defaultmap(array):
    filename = '1301_default.map'
    newFName = 'default.map'
    
    file = open(filename, 'r+')
    
    with open(newFName, 'w') as output:
        for line in file:
            for i in range(0,len(array)):
                line = line.replace(array[i][1],'')
            output.write(line)
    cn_names_english(array)
            
def cn_names_english(array):
    filename = '1301.yml'
    newFName = 'cn_names_english.yml'
    array2 = []
    
    file = open(filename, 'r+', encoding='utf8')
    
    
    with open(newFName, 'w', encoding='utf8') as output:
        for i in range(0,len(array)):
            arrayN = []
            arrayN.append(array[i][0])
            array2.append(arrayN)
        for line in file:
            for i in range(0,len(array2)):
                fline = line.find(' '+array2[i][0]+':')
                if fline >= 0:
                    array2[i].append(line[line.find('"')+1:-2])
        #output.write('l_english:\n')
        four = 3004
        for i in range(0,len(array2)):
            output.write(' CN'+array2[i][0]+':0 "'+array2[i][1]+'"\n')
            output.write(' colonial_'+array2[i][0]+'_region:0 "Colonial '+array2[i][1]+'"\n')
            output.write(' trade_company_tc'+array2[i][0]+':0 "'+array2[i][1]+' Charter"\n')
            output.write(' TRADE_COMPANY_'+array2[i][0].upper()+'_Root_Culture_GetName:0 "[Root.Culture.GetName] '+array2[i][1]+' Company"\n')
            output.write(' TRADE_COMPANY_'+array2[i][0].upper()+'_Trade_Company:0 "'+array2[i][1]+' Trade Company"\n')
            output.write(' colonial_cn'+array2[i][0]+':0 "Colonial '+array2[i][1]+'"\n')
            output.write(' COLONIAL_'+array2[i][0].upper()+'_Root_Culture_GetName_'+array2[i][0].capitalize()+':0 "[Root.GetAdjective] '+array2[i][1]+'"\n')
            output.write(' COLONIAL_'+array2[i][0].upper()+'_Root_Culture_GetName_'+array2[i][0].capitalize()+'_ADJ:0 "[Root.GetAdjective] '+array2[i][1]+'"\n')
            output.write(' flavor_cn.'+str(four)+':0 "New Territory in '+array2[i][1]+'"\n \n')
            four += 1
    
    print(array2)
    
start2()