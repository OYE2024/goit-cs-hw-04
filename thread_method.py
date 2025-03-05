import threading
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
result = {}
lock = threading.Lock()


def search_in_file(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            content = file.read().lower()
            local_result = {key: [] for key in key_words}

            for key in key_words:
                if key in content:
                    local_result[key].append(path)

            with lock:
                for key, files in local_result.items():
                    if files:
                        if key not in result:
                            result[key] = []
                        result[key].extend(files)

    except FileNotFoundError:
        print(f"File not found: {path}")
    except Exception as e:
        print(f"Error while reading the file {path}: {e}")


def search_key_word_multithreaded():
    start_time = time.time()

    threads = []
    for path in paths_to_documents:
        thread = threading.Thread(target=search_in_file, args=(path,))
        threads.append(thread)
        thread.start()

    # Ожидание завершения всех потоков
    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Work time is: {end_time - start_time:.6f} seconds")
    return result


if __name__ == '__main__':
    search_results = search_key_word_multithreaded()
    print(json.dumps(search_results, indent=4, ensure_ascii=False))
