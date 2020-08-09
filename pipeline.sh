#!/bin/bash
echo '--------------------------'
echo 'Pipeline Execution'
echo '##################'

echo 'Defining variables input'

pedidos='../dataset/pedidos'
visitas='../dataset/visitas'
produtos='../dataset/produtos.csv'
saida='../../saida'
data_inicial='01/06/2020'
data_final='02/06/2020'
departamentos='alimentos,audio,musica,pet_shop,pc_gamer,pcs'
saida_normalizacao='../../saida-normalizacao'
saida_cluster='../../saida-cluster'
number_of_cluster=2
saida_graphs='../../saida-graphs.html'
x_axis='convertido'
y_axis='pet_shop'
cluster_label='0'

echo '##################'

echo 'Initializing pipeline' &&
echo 'Step 1: Create dataframes' &&
python3 ./desafio_iafront/jobs/pedidos/job_pedidos.py \
  --pedidos $pedidos \
  --visitas $visitas \
  --produtos $produtos \
  --saida $saida \
  --data-inicial $data_inicial \
  --data-final $data_final &&

echo 'Step 2: Normalizing data' &&
python3 ./desafio_iafront/jobs/escala_pedidos/job_normalizacao.py \
  --departamentos $departamentos \
  --visitas-com-conversao $saida \
  --saida $saida_normalizacao \
  --data-inicial $data_inicial \
  --data-final $data_final &&

echo '--------------------------' &&


echo 'Step 3: Clustering result' &&
python3 ./desafio_iafront/jobs/clusters/job_kmeans.py \
  --dataset $saida_normalizacao \
  --saida $saida_cluster \
  --number_of_cluster $number_of_cluster \
  --data-inicial $data_inicial \
  --data-final $data_final &&

echo '--------------------------' &&

echo 'Step 4: Plotting graphs' &&
python3 ./desafio_iafront/jobs/graphics/job_graphics.py \
  --dataframe-path $saida_normalizacao \
  --saida $saida_graphs \
  --x_axis $x_axis \
  --y_axis $y_axis \
  --cluster_label $cluster_label \
  --data-inicial $data_inicial \
  --data-final $data_final &&

echo '--------------------------'
echo 'Finishing Pipeline'
echo '--------------------------'
