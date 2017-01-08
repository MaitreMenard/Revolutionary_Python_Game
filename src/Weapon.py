from resources.weapons import WEAPONS

class Weapon:
    
    def __init__(self, name):
        assert isinstance(name, str)
        self.is_equipped = False
        """
        TODO: si la référence au Character n'est utile que pour déterminer sa classe,
        remplacer cette attribut par le nom de la classe du Character en string
        """
        self.owner = None
        self.__dict__.update(WEAPONS[name])
    
    def toggle_equip(self):
        if self.is_equipped:
            self.is_equipped = False
            actions = self.on_unequip
        else:
            self.is_equipped = True
            actions = self.on_equip
        
        for action in actions:
            if action["type"] == "check":
                self.check(action)
            elif action["type"] == "action":
                self.action(action)
    
    def check(self, dic):
        """Check a condition and call an action according to it"""
        assert isinstance(dic, dict)
        obj = getattr(self, dic["condition"]["object"])
        compared_attr = getattr(obj, dic["condition"]["attribute"])
        value = dic["condition"]["value"]
        result = compared_attr == value
        
        self.action(*dic[result])
        
    def action(self, *dicts):
        assert(all(type(dic)==dict for dic in dicts))
        for dic in dicts:
            act = getattr(self, dic["action"])
            args = dic["args"]
            if isinstance(args, list):
                act(*args)
            elif isinstance(args, dict):
                act(**args)
    
    def set_attribute(self, field, value):
        setattr(self, field, value)
        
    def add_to(self, category, actions):
        action_lists = getattr(self, category)        
        for action in actions:
            if action not in action_lists:
                action_lists.append(action)
                
    def remove_from(self, category, actions):
        action_lists = getattr(self, category)
        for action in actions:
            if action in action_lists:
                action_lists.remove(action)
        