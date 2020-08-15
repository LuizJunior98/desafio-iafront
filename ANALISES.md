## Análises

1. Usando uma semana de dados como entrada e vendo os gráficos, o que você pode dizer sobre cada uma das transformações?
> Cada transformação tem seu próprio objetivo, sabendo disso, inciei minha análise utilizando apenas o normalizer a fim de tentar entender a distribuição dos dados no periodo de uma semana.
> Em seguida, entendendo que não se tratava de uma distribuição normal, resolvi aplicar as técnicas de PowerTransformation e MinMaxScale a fim de aproximar a distribuição de uma normal, abrindo caminho para a aplicação de StandartScale a fim de simplificar ainda mais o comportamento.
> Encerrei o estudo, aplicando a técnica de RobustScale a fim de reduzir o impacto dos outliers.
>
> Cada transformação teve seu papel fundamental, mas os resultados não se alteraram tanto, permanecendo bem similar. Por exemplo, se analisarmos os dados de pet_shop podemos concluir que pouco mais de 50% das pessoas que observaram algum produto dentro dos departamentos [alimentos, audio, musica, pet_shop, pc_gamer, pcs, cama_mesa_banho] compraram algo de pet_shop.
2. Use uma semana diferente, o que você viu mudando?
> Usando uma semana diferente e pegando o mesmo exemplo (pet_shop) como base, ficou evidente uma queda da conversão de produtos desse departamento mesmo com uma média de acesso similar ao da primeira semana analisada
3. Quais colunas escolheu para gerar suas análises, e por quê?
> As colunas escolhidas foram departamento (exemplo: pet_shop) e convertido, pois a ideia era tentar analisar a qual a probabilidade de um cliente observar algum produto desse departamento e realizar uma compra no mesmo
4. Quais colunas sofreram maiores efeitos e quais sofreram menos?
> A coluna que mais sofreu impacto foi convertido, pois logicamente era a mais alterada de acordo com o departamento escolhido

##

1. Quais clusters têm problemas para serem analisados?
> O mean_shift devido a demora no processamento do mesmo
2. Quais clusters têm uma evolução ruim ao longo do tempo, e quais têm uma evolução boa.
> O melhor cluster entre todos os testados foi o kmeans, por apresentar uma praticidade na sepração com base na quantidade de registros
3. Quais clusters você considera que precisam de mais investimento para ampliar a conversão?
> O kmeans
4. Você consegue identificar algum fenômeno temporal que gere destaque a um ou mais clusters?
> O cluster mean_shift foi o que mais demorou para ser executado.