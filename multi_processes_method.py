import multiprocessing
import time
import json

paths_to_documents = [
    r'G:\Мой диск\Data_Science_education\GoIT\Home_works\Computer-Systems-and-Their-Fundamentals\CompSys_Lesson_8\test_1.txt',
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

key_words = ['trend', 'trends', 'IT', 'programming', 'AI', 'cybersecurity']


def search_in_file(path):
    local_result = {}

    try:
        with open(path, "r", encoding="utf-8") as file:
            content = file.read().lower()
            for key in key_words:
                if key in content:
                    if key not in local_result:
                        local_result[key] = []
                    local_result[key].append(path)
    except FileNotFoundError:
        print(f"File not found: {path}")
    except Exception as e:
        print(f"Error while reading the file {path}: {e}")

    return local_result


def merge_results(results):
    final_result = {}
    for res in results:
        for key, files in res.items():
            if key not in final_result:
                final_result[key] = []
            final_result[key].extend(files)
    return final_result


def search_key_word_multiprocessing():
    start_time = time.time()

    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(search_in_file, paths_to_documents)

    final_result = merge_results(results)

    end_time = time.time()
    print(f"Work time is: {end_time - start_time:.6f} seconds")
    return final_result


if __name__ == '__main__':
    search_results = search_key_word_multiprocessing()
    print(json.dumps(search_results, indent=4, ensure_ascii=False))
