from os import system
import psutil
from pypresence import Presence
import time
import sys
import discord
import asyncio
import colorama
from colorama import Fore, init, Style
import platform
from cloner import Clone

version = '0.2'


def clearall():
    system('clear')
    print(f"""{Style.BRIGHT}{Fore.GREEN}
░██████╗░░█████╗░███╗░░░███╗███████╗██████╗░  ░█████╗░░█████╗░██████╗░███████╗██╗░░██╗
██╔════╝░██╔══██╗████╗░████║██╔════╝██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗██╔════╝╚██╗██╔╝
██║░░██╗░███████║██╔████╔██║█████╗░░██████╔╝  ██║░░╚═╝██║░░██║██║░░██║█████╗░░░╚███╔╝░
██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░██╔══██╗  ██║░░██╗██║░░██║██║░░██║██╔══╝░░░██╔██╗░
╚██████╔╝██║░░██║██║░╚═╝░██║███████╗██║░░██║  ╚█████╔╝╚█████╔╝██████╔╝███████╗██╔╝╚██╗
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝  ░╚════╝░░╚════╝░╚═════╝░╚══════╝╚═╝░░╚═╝
                                    ~ Developed by Criminal Coder
{Style.RESET_ALL}{Fore.MAGENTA}{Fore.RESET}""")


client = discord.Client()
os = platform.system()
if os == "Windows":
    system("cls")
else:
    print(chr(27) + "[2J")
    clearall()
while True:
    token = input(
        f'{Style.BRIGHT}{Fore.MAGENTA}Paste your token{Style.RESET_ALL}{Fore.RESET}\n >'
    )
    guild_s = input(
        f'{Style.BRIGHT}{Fore.MAGENTA}Provide server ID which you have to clone{Style.RESET_ALL}{Fore.RESET}\n >'
    )
    guild = input(
        f'{Style.BRIGHT}{Fore.MAGENTA}Provide your server ID{Style.RESET_ALL}{Fore.RESET}\n>'
    )
    clearall()
    print(f'{Style.BRIGHT}{Fore.GREEN}The entered values are:')
    print(
        f'{Style.BRIGHT}{Fore.GREEN}Your token: {Fore.YELLOW}{token}{Style.RESET_ALL}{Fore.RESET}'
    )
    print(
        f'{Style.BRIGHT}{Fore.GREEN}Server ID to replicate: {Fore.YELLOW}{guild_s}{Style.RESET_ALL}{Fore.RESET}'
    )
    print(
        f'{Style.BRIGHT}{Fore.GREEN}Server ID you want to paste the copied server: {Fore.YELLOW}{guild}{Style.RESET_ALL}{Fore.RESET}'
    )

    confirm = input(
        f'{Style.BRIGHT}{Fore.MAGENTA}Are the values correct? {Fore.YELLOW}(Y/N){Style.RESET_ALL}{Fore.RESET}\n >'
    )

    if confirm.upper() == 'Y':
        if not guild_s.isnumeric():
            clearall()
            print(
                f'{Style.BRIGHT}{Fore.RED}Server ID to replicate must only contain numbers.{Style.RESET_ALL}{Fore.RESET}'
            )
            continue
        if not guild.isnumeric():
            clearall()
            print(
                f'{Style.BRIGHT}{Fore.RED}The destination server ID must only contain numbers.{Style.RESET_ALL}{Fore.RESET}'
            )
            continue
        if not token.strip() or not guild_s.strip() or not guild.strip():
            clearall()
            print(
                f'{Style.BRIGHT}{Fore.RED}One or more fields are blank.{Style.RESET_ALL}{Fore.RESET}'
            )
            continue
        if len(token.strip()) < 3 or len(guild_s.strip()) < 3 or len(
                guild.strip()) < 3:
            clearall()
            print(
                f'{Style.BRIGHT}{Fore.RED}One or more fields are less than 3 characters long.{Style.RESET_ALL}{Fore.RESET}'
            )
            continue
        break
    elif confirm.upper() == 'N':
        clearall()
    else:
        clearall()
        print(
            f'{Style.BRIGHT}{Fore.RED}Invalid option. Please enter Y or N.{Style.RESET_ALL}{Fore.RESET}'
        )

input_guild_id = guild_s
output_guild_id = guild
token = token
clearall()


@client.event
async def on_ready():
    try:
        print(
            f"{Style.BRIGHT}{Fore.GREEN} Account authentication was successful"
        )
        print(
            f"{Style.BRIGHT}{Fore.BLUE} Clone Version: {Fore.YELLOW}{version}{Style.RESET_ALL}{Fore.RESET}"
        )
        print(
            f"{Style.BRIGHT}{Fore.BLUE} Discord.py API version in use: {Style.BRIGHT}{Fore.YELLOW}{discord.__version__}{Style.RESET_ALL}{Fore.RESET}"
        )
        print(
            f"{Style.BRIGHT}{Fore.BLUE} Hello, {Fore.YELLOW}{client.user.name}!{Fore.BLUE} Cloning will begin in a moment...{Style.RESET_ALL}{Fore.RESET}"
        )
        print(f"\n")
        guild_from = client.get_guild(int(input_guild_id))
        guild_to = client.get_guild(int(output_guild_id))
        await Clone.guild_edit(guild_to, guild_from)
        await Clone.roles_delete(guild_to)
        await Clone.channels_delete(guild_to)
        await Clone.roles_create(guild_to, guild_from)
        await Clone.categories_create(guild_to, guild_from)
        await Clone.channels_create(guild_to, guild_from)
        print(f"{Style.BRIGHT}{Fore.GREEN}The server has been copied successfully!")
        print(
            f"{Style.BRIGHT}{Fore.BLUE}Leave a star on our repo: {Fore.YELLOW}https://github.com/Criminal-Coder/Discord-Server-Cloner.git{Style.RESET_ALL}"
        )
        print(
            f"{Style.BRIGHT}{Fore.BLUE}Finishing process and logging out of account {Fore.YELLOW}{client.user}"
        )
        await client.close() 
    except discord.LoginFailure:
        print(
            "Unable to authenticate to account. Check that the token is correct."
        )
    except discord.Forbidden:
        print(
            "Cloning could not be performed due to insufficient permissions."
        )
    except discord.HTTPException:
        print("There was an error communicating with the Discord API.")
    except discord.NotFound:
        print(
            "It was not possible to find any of the copy elements (channels, categories, etc.)."
        )
    except Exception as e:
        print(f"Error in on_ready function: {e}")


client.run(token, bot=False)
