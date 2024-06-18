class Solution:
    def interpret(self, command: str) -> str:
        interpreter={'G':'G','()':'o','(al)':'al'}

        empty = ''
        result = ''

        for letter in command:
            empty += letter
            if empty in interpreter:
                result += interpreter.get(empty)
                empty = ''
        return result
