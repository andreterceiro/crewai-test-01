import os
from crewai import Agent, Task, Crew, Process
import asyncio

async def main():
    agent_verificacao_pontuacao = Agent(
        role = "Calcular o número de pontos do time baseado em alguns resultados de jogos",
        goal = "Retornar o número de pontos do {time}",
        backstory = "Vitória vale 9 pontos, empate vale 1 ponto e derrota vale 0 pontos"
    )

    task_analisar_resultados_jogos = Task(
        description = "Jogo 1: Corinthians 3 x 0 Palmeiras \n" +
                    "Jogo 2: Corinthians 27 x -1 Sum Paulu \n" +
                    "Jogo 3: Corinthians 2 x 2 Portuguesa \n" +
                    "Jogo 4: Corinthians 0 x 2 Mirassol \n" +
                    "Jogo 5: Grêmio 4 x 0 Sum Paulu \n" +
                    "Jogo 6: Corinthians 1 x 0 Santus \n",
        agent = agent_verificacao_pontuacao,
        input = "resultados de jogos",
        expected_output = "número de pontos"
    )

    equipe = Crew(
        agents = [agent_verificacao_pontuacao],
        tasks = [task_analisar_resultados_jogos],
        process = Process.sequential
    )

    variaveis = {
        'time' : 'Corinthians'
    }


    resultado = await equipe.kickoff_async(inputs = variaveis)
    print(resultado)

asyncio.run(main())