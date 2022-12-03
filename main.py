#imports
import interactions
import random
import cloudscraper

#settings
SafeMines = ':white_check_mark:'
TileMines = ':x:'
SafeTowers = ':white_check_mark:'
TileTowers = ':x:'
BotToken = ''
ServerId = 0
BuyerRoleId = 0

#StartUp
bot = interactions.Client(
  token=BotToken                               
)

#defines
def GenGrid(SafeTiles:int):
    Generating = True
    BoardNums = []
    Board = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    Grid = f''
    line = 0
    endrownums = [6,11,16,21]
    while Generating:
        if len(BoardNums) < SafeTiles:
            Selection = random.randint(1, 25)
            if Selection in BoardNums:
                pass
            else:
                BoardNums.append(Selection)
        else:
            Generating = False
    for Number in BoardNums:
        Board[Number-1] = 1
    for Position in Board:
        line += 1
        if line in endrownums:
            Grid += f'\n'
            if Position == 1:
                Grid += f'{SafeMines}'
            else:
                Grid += f'{TileMines}'
        else:
            if Position == 1:
                Grid += f'{SafeMines}'
            else:
                Grid += f'{TileMines}'
    return Grid


def gentower(rows:int):
    if rows >= 9:
        return "Max Rows 8!"
    else:
        def pr():
            rowtp1 = f"{SafeTowers}{TileTowers}{TileTowers}"
            rowtp2 = f"{TileTowers}{SafeTowers}{TileTowers}"
            rowtp3 = f"{TileTowers}{TileTowers}{SafeTowers}"
            joe = random.randint(1,3)
            if joe == 1:
                return rowtp1
            elif joe == 2:
                return rowtp2
            else:
                return rowtp3
        leg = True
        counter = 0
        finaltower = f""
        while leg:
            if counter == rows:
                leg = False
            else:
                counter +=1
                finaltower += f"{pr()}\n"

        return finaltower




#Commands
@bot.command(
    name='mines',
    description="Generates A Mine Grid",
    scope=ServerId,
    options= [
        interactions.Option(
            name="game_id",
            description="Put your game id here",
            type=interactions.OptionType.STRING,
            required=True,
        ),
        interactions.Option(
            name="clicks",
            description="How many safe spots to generate",
            type=interactions.OptionType.INTEGER,
            required=True,
        )
    ]
)
async def Mines(ctx, game_id: str, clicks:int):
    if BuyerRoleId in ctx.author.roles or ctx.author.id == 756534114143961088:
        if int(clicks) > 23:
            mines = interactions.Embed(title=f"Mines", description=f"Too Many SafeClicks! Max is 23\nYou Chose {clicks}/23", color=0xFC4431)
            await ctx.send(embeds=mines, ephemeral=True)
        else:
            count = 0
            includes_dash = False
            includes_number1 = ""
            includes_number2 = ""
            for v in game_id:
                count += 1
                if count == 9:
                    if v == "-":
                        includes_dash = True
                if count == 15:
                    includes_number1 += v
                if count == 22:
                    includes_number2 +=v
            if includes_dash == True:
                if includes_number1 == "4":
                    try:
                        int(includes_number2)
                        mines = interactions.Embed(title=f"Mines", description=f"Generated Tiles!", color=0xFC4431)
                        mines.add_field(name=f"Field {clicks} Clicks", value=GenGrid(clicks),inline=True)
                        await ctx.send(embeds=mines, ephemeral=True)
                        print(f"\n\n{ctx.author} Used Towers command\nID = {ctx.author.id}\n")
                    except ValueError:
                        mines = interactions.Embed(title=f"Mines", description=f"Invalid ID!", color=0xFC4431)
                        await ctx.send(embeds=mines, ephemeral=True)
                else:
                    mines = interactions.Embed(title=f"Mines", description=f"Invalid ID!", color=0xFC4431)
                    await ctx.send(embeds=mines, ephemeral=True)
            else:
                mines = interactions.Embed(title=f"Mines", description=f"Invalid ID!", color=0xFC4431)
                await ctx.send(embeds=mines, ephemeral=True)
    else:
        await ctx.send(f"Not Eligable! {ctx.author.mention}")

@bot.command(
    name='towers',
    description="Generates A Tower Grid",
    scope=ServerId,
    options= [
        interactions.Option(
            name="game_id",
            description="Put your game id here",
            type=interactions.OptionType.STRING,
            required=True,
        ),
        interactions.Option(
            name="rows",
            description="How many rows to generate",
            type=interactions.OptionType.INTEGER,
            required=True,
        )
    ]
)
async def Towers(ctx, game_id: str, rows:int):
    if BuyerRoleId in ctx.author.roles or ctx.author.id == 756534114143961088:
        if int(rows) > 8:
            towers = interactions.Embed(title=f"Towers", description=f"Too Many Rows! Max is 8\nYou Chose {rows}/8", color=0xFC4431)
            await ctx.send(embeds=towers, ephemeral=True)
        else:
            count = 0
            includes_dash = False
            includes_number1 = ""
            includes_number2 = ""
            for v in game_id:
                count += 1
                if count == 9:
                    if v == "-":
                        includes_dash = True
                if count == 15:
                    includes_number1 += v
                if count == 22:
                    includes_number2 +=v
            if includes_dash == True:
                if includes_number1 == "4":
                    try:
                        int(includes_number2)
                        towers = interactions.Embed(title=f"Towers", description=f"Generated Tower!", color=0xFC4431)
                        towers.add_field(name=f"Field {rows} Rows", value=gentower(rows),inline=True)
                        await ctx.send(embeds=towers, ephemeral=True)
                        print(f"\n\n{ctx.author} Used Towers command\nID = {ctx.author.id}\n")
                    except ValueError:
                        towers = interactions.Embed(title=f"Towers", description=f"Invalid ID!", color=0xFC4431)
                        await ctx.send(embeds=towers, ephemeral=True)
                else:
                    towers = interactions.Embed(title=f"Towers", description=f"Invalid ID!", color=0xFC4431)
                    await ctx.send(embeds=towers, ephemeral=True)
            else:
                towers = interactions.Embed(title=f"Towers", description=f"Invalid ID!", color=0xFC4431)
                await ctx.send(embeds=towers, ephemeral=True)

    else:
        await ctx.send(f"Not Eligable! {ctx.author.mention}")
@bot.command(
    name='crash',
    description="Predict a Crash Game",
    scope=ServerId
)
async def crash(ctx):
    if BuyerRoleId in ctx.author.roles or ctx.author.id == 756534114143961088:
        scraper = cloudscraper.create_scraper()
        print(f"{ctx.author} Used command\nID = {ctx.author.id}\n\n")
        games = scraper.get("https://rest-bf.blox.land/games/crash").json()
        previousGame = games["history"][0]["crashPoint"]
        gameId = games["current"]["_id"]
        av2 = (games["history"][0]["crashPoint"] + games["history"][1]["crashPoint"])
        chancenum = 100/previousGame
        estnum = (1 / (1 - chancenum) + av2) / 2
        estimate = ("{:.2f}".format(round(estnum, 2)))
        chance = ("{:.2f}".format(round(chancenum, 2)))
        event = interactions.Embed(title=f"Crash", description=f"{ctx.author.mention}", color=0xFC4431)
        event.add_field(name="Crash Estimate", value=f"```{estimate}X```", inline=False)
        event.add_field(name="Game ID", value=f"```{gameId}```", inline=False)
        event.add_field(name="Chance", value=f"```{chance}/100 Chance its correct```", inline=False)
        await ctx.send(embeds=event, ephemeral=True)
        print(f"\n\n{ctx.author} Used Crash command\nID = {ctx.author.id}\nCrash: {estimate} GameID: {gameId}\n")
    else:
        await ctx.send(f"Not Eligable! {ctx.author.mention}")

#Bot
bot.start()
