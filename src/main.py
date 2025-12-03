import asyncio

from constants import QUERY_PARAMS
from parser import run_parser
from utils import generate_url, get_options_list


def print_summary(keyword: str, exp_level: str):
    print(
        f"""
Chosen options:

Category: {keyword}
Experience: {exp_level} and below
"""
    )


def ask_option(title: str, arr: list[str]) -> str:
    print(title + get_options_list(arr))
    idx = int(input("Enter a number: "))
    return arr[idx - 1]


def start():
    try:
        keyword = ask_option(
            "Choose category you want to parse:", QUERY_PARAMS["primary_keyword"]
        )
        exp_level = ask_option(
            "Choose experience level (everything below will be included):",
            QUERY_PARAMS["exp_level"],
        )

        print_summary(keyword, exp_level)

        if input("Start parsing? (y/n)\n").lower() == "y":
            url = generate_url(keyword, exp_level)

            asyncio.run(run_parser(url))
        else:
            print("exit")

    except Exception as e:
        print(f"\nError: {e}")
        print("fuck you, I quit")
        return


if __name__ == "__main__":
    start()
