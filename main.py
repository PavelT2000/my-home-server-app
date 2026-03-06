import multiprocessing
import uvicorn
import os
import sys

def run_website():
    print(" [Web] Запуск фронтенда на порту 8000...")
    # Добавляем путь к папке webSite в PATH этого процесса
    sys.path.append(os.path.join(os.getcwd(), "webSite"))
    # Переходим в саму папку, чтобы jinja2 видела папку /templates
    os.chdir(os.path.join(os.getcwd(), "webSite"))
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)

def run_ai_service():
    print(" [AI] Запуск ИИ-сервиса на порту 8001...")
    # Добавляем путь к папке ai_service в PATH этого процесса
    sys.path.append(os.path.join(os.getcwd(), "ai_service"))
    # Переходим в папку, чтобы импорты типа 'from ai_logic' работали
    os.chdir(os.path.join(os.getcwd(), "ai_service"))
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=False)

if __name__ == "__main__":
    multiprocessing.freeze_support()
    
    # Используем 'spawn', чтобы процессы были максимально чистыми и изолированными
    try:
        multiprocessing.set_start_method('spawn', force=True)
    except RuntimeError:
        pass

    process_web = multiprocessing.Process(target=run_website)
    process_ai = multiprocessing.Process(target=run_ai_service)

    try:
        process_web.start()
        process_ai.start()
        
        process_web.join()
        process_ai.join()
    except KeyboardInterrupt:
        print("\n [!] Выключение...")
        process_web.terminate()
        process_ai.terminate()