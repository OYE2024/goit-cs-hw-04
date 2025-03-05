import time
import json

paths_to_documents = [r'G:\Мой диск\Data_Science_education\GoIT\Home_works\Computer-Systems-and-Their-Fundamentals\CompSys_Lesson_8\test_1.txt',
                      r'G:\Мой диск\Data_Science_education\GoIT\Home_works\Computer-Systems-and-Their-Fundamentals\CompSys_Lesson_8\test_2.txt',
                      r'G:\Мой диск\Data_Science_education\GoIT\Home_works\Computer-Systems-and-Their-Fundamentals\CompSys_Lesson_8\test_3.txt',
                      r'G:\Мой диск\Data_Science_education\GoIT\Home_works\Computer-Systems-and-Their-Fundamentals\CompSys_Lesson_8\test_4.txt',
                      r'G:\Мой диск\Data_Science_education\GoIT\Home_works\Computer-Systems-and-Their-Fundamentals\CompSys_Lesson_8\test_5.txt',
                      r'G:\Мой диск\Data_Science_education\GoIT\Home_works\Computer-Systems-and-Their-Fundamentals\CompSys_Lesson_8\test_6.txt',
                      r'G:\Мой диск\Data_Science_education\GoIT\Home_works\Computer-Systems-and-Their-Fundamentals\CompSys_Lesson_8\test_7.txt',
                      r'G:\Мой диск\Data_Science_education\GoIT\Home_works\Computer-Systems-and-Their-Fundamentals\CompSys_Lesson_8\test_8.txt',
                      r'G:\Мой диск\Data_Science_education\GoIT\Home_works\Computer-Systems-and-Their-Fundamentals\CompSys_Lesson_8\test_9.txt',
                      r'G:\Мой диск\Data_Science_education\GoIT\Home_works\Computer-Systems-and-Their-Fundamentals\CompSys_Lesson_8\test_10.txt'
                      ]


def search_key_word():
    start_time = time.time()
    try:
        key_words = ['trend', 'trends', 'IT',
                     'programming', 'AI', 'cybersecurity']
        result = {}

        for path in paths_to_documents:
            try:
                with open(path, "r", encoding="utf-8") as file:
                    content = file.read().lower()
                    for key in key_words:
                        if key.lower() in content:
                            if key not in result:
                                result[key] = []
                            result[key].append(path)
            except FileNotFoundError:
                print(f"File not found: {path}")

        end_time = time.time()
        print(f"Work time is: {end_time - start_time:.6f} seconds")
        return result

    except Exception as e:
        print(f"An error occurred: {e}")
        return {}


if __name__ == '__main__':
    search_results = search_key_word()
    print(json.dumps(search_results, indent=4, ensure_ascii=False))
