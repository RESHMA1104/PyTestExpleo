import logging

def log_generator():

    logger = logging.getLogger("AutomationLogger")

    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers
    if logger.handlers:
        logger.handlers.clear()

    # File Handler
    file_handler = logging.FileHandler("testlogreport.log")
    file_handler.setLevel(logging.INFO)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger