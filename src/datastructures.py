
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
                'id': self._generateId(),
                'first_name': 'john',
                'last_name': 'jackson',
                'age': 33,
                'lucky numbers': [7, 13, 22]
            },


           {
                'id': self._generateId(),
                'first_name': 'jane',
                'last_name': 'jackson',
                'age': 35,
                'lucky numbers': [10, 14, 3]
            },

            {
                'id': self._generateId(),
                'first_name': 'jimmy',
                'last_name': 'jackson',
                'age': 5,
                'lucky numbers': [1]
            },

            


        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        # push
        self._members.append(member)
        return None
       

    def delete_member(self, id):
        # fill this method and update the return
        # need a for loop to find a specific family member id to remove
        for member in self._members:
            if member['id'] == id:
               self._members.pop(member)
            return None
        pass


    def get_member(self, id):
        # fill this method and update the return
        # need a for loop to retrieve a specific family member id to display
        for member in self._members:
            if member['id'] == id:
                return member
        pass

    # this method is done, it returns a list with all the family members

    def get_all_members(self):
        return self._members
