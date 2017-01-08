# TODO: possibilité de remplacer ce dictionnaire par un XML ou un JSON
WEAPONS = {
    "iron longsword": {
        "type": "sword",
        "category": "2h",
        "rank": "e",
        "durability": 40,
        "dmg": 3,
        "hit": 100,
        "crit": 0,
        "price": 400,
        "magic": 0,
        
        "on_hit_actions": [],
        "on_turn_actions": [],
        "on_equip": [],
        "on_unequip": []
    },
           
    "steel longsword": {
        "type": "sword",
        "category": "2h",
        "rank": "d",
        "durability": 35,
        "dmg": 5,
        "hit": 90,
        "crit": 0,
        "price": 875,
        "magic": 0,
        
        "on_hit_actions": [],
        "on_turn_actions": [],
        "on_equip": [],
        "on_unequip": []               
    },
           
    "thief's blade": {
        "type": "sword",
        "category": "1h",
        "rank": "d",
        "durability": 40,
        "dmg": 2,
        "hit": 80,
        "crit": 0,
        "price": 1000,
        "magic": 0,
        
        "on_hit_actions": [],
        "on_turn_actions": [],
        "on_equip": [
            {
                "type": "check",
                "condition": {
                    "object": "owner",
                    "attribute": "char_class",
                    "value": "thief"
                },
                True: [
                    {
                        "type": "action",
                        "action": "set_attribute",
                        "args": {
                            "field": "dmg",
                            "value": 5
                        }
                    },
                    {
                        "type": "action",
                        "action": "set_attribute",
                        "args": {
                            "field": "hit",
                            "value": 100
                        }
                    },
                    {
                     
                        "type": "action",
                        "action": "set_attribute",
                        "args": {
                            "field": "crit",
                            "value": 10
                        }
                    },   
                    {                     
                        "type": "action",
                        "action": "set_attribute",
                        "args": {
                            "field": "magic",
                            "value": 1
                        }
                    },
                    {
                        "type": "action",
                        "action": "add_to",
                        "args": {
                            "category": "on_hit_actions",
                            "actions": ["poison"]
                        }
                    }
                ],
             
                False: []
            }
        ],
        "on_unequip": [
            {
                "type": "action",
                "action": "set_attribute",
                "args": {
                    "field": "dmg",
                    "value": 2
                }
            },      
            {
                "type": "action",
                "action": "set_attribute",
                "args": {
                    "field": "hit",
                    "value": 80
                }
            },       
            {
                     
                "type": "action",
                "action": "set_attribute",
                "args": {
                    "field": "crit",
                    "value": 0
                }
            },       
            {                     
                "type": "action",
                "action": "set_attribute",
                "args": {
                    "field": "magic",
                    "value": 0
                }
            },
            {
                "type": "action",
                "action": "remove_from",
                "args": {
                    "category": "on_hit_actions",
                    "actions": ["poison"]
                }
            }
        ]
    }
}