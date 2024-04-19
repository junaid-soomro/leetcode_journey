class Solution:
    def defangIPaddr(self, address: str) -> str:
        address_as_list = list(address)
        for index in range(len(address)):
            current_char = address[index]
            if(current_char == '.'):
                address_as_list[index] = "[.]"
        
        return "".join(address_as_list)
