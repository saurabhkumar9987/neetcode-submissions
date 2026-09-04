class TextProcessor:
    # Implement method overloading for format_text method
    def format_text(self, text1: str, text2: str = "") -> str:
        return (text1+text2).upper()

    def format_texted(self,text1,text2): 
        return (text1 + text2)




# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_texted("hello", "world"))
