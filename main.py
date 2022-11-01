"""Driver file for the bot"""
from utility import *

def parse(essay: str, paragraph_count: int) -> None:
    """
    :param essay: string to check rules against.
    :param paragraph_count: paragraph number.
    """
    if not check_num_sentences_in_paragraph(essay, paragraph_count): return False
    if not check_past_tense(essay, paragraph_count): return False
    
    return True

def main():
    print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to start parsing.")
    paragraphs = []
    while True:
        try:
            paragraph = input()
        except EOFError:
            break
        paragraphs.append(paragraph)

    N = len(paragraphs)
    for i in range(N):
        if not parse(paragraphs[i], i):
            return 

    print(f'{bcolors.OKGREEN}All checks passed!')

if __name__ == "__main__":
    main()