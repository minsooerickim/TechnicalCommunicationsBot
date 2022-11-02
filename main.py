"""Driver file for the bot"""
from distutils.log import error
from utility import *

def parse(essay: str) -> None:
    """
    :param essay: string to check rules against.
    """
    error_detected = False
    if not check_num_sentences_in_paragraph(essay): error_detected = True
    if not check_past_tense(essay): error_detected = True
    if not word_count_per_sentence(essay): error_detected = True
    
    return not error_detected

def main():
    print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to start parsing.")
    paragraphs = []
    while True:
        try:
            paragraph = input()
        except EOFError:
            break
        paragraphs.append(paragraph)

    error_detected = False  
    N = len(paragraphs)
    for i in range(N):
        if not parse(paragraphs[i]): error_detected = True
    
    if not error_detected:
        print('\n')
        print(f'{bcolors.OKGREEN}All checks have passed!')
    print('\n')

if __name__ == "__main__":
    main()