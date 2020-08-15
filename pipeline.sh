#!/bin/bash
echo '--------------------------'
echo 'Pipeline Execution'
echo '##################'

echo 'Defining variables input'

create_new_dataframe=1
pedidos='../dataset/pedidos'
visitas='../dataset/visitas'
produtos='../dataset/produtos.csv'
saida='../desafio-iafront-result/saida'
data_inicial='08/06/2020'
data_final='16/06/2020'
departamentos='alimentos,audio,musica,pet_shop,pc_gamer,pcs,cama_mesa_banho'
saida_normalizacao='../desafio-iafront-result/saida-normalizacao'
normalize_technical='normalizer'
saida_cluster='../desafio-iafront-result/saida-cluster/kmeans'
# shellcheck disable=SC2034
saida_cluster_mean_shift='../desafio-iafront-result/saida-cluster/mean-shift'
# shellcheck disable=SC2034
saida_cluster_dbscan='../desafio-iafront-result/saida-cluster/dbscan'
# shellcheck disable=SC2034
saida_cluster_optical='../desafio-iafront-result/saida-cluster/optical'
# shellcheck disable=SC2034
saida_cluster_spectral='../desafio-iafront-result/saida-cluster/spectral'
number_of_cluster=2
saida_graphs='../desafio-iafront-result/saida-graphs.html'
x_axis='convertido'
y_axis='pet_shop'

echo '##################'

echo 'Initializing pipeline'
if [ $create_new_dataframe -eq 1 ]
then
    echo 'Step 1: Create dataframes' &&
    python3 ./desafio_iafront/jobs/pedidos/job_pedidos.py \
      --pedidos $pedidos \
      --visitas $visitas \
      --produtos $produtos \
      --saida $saida \
      --data-inicial $data_inicial \
      --data-final $data_final
else
    echo '----------->'
    echo 'Pass Step 1'
    echo '----------->'
fi &&

echo 'Step 2: Normalizing data' &&
python3 ./desafio_iafront/jobs/escala_pedidos/job_normalizacao.py \
  --departamentos $departamentos \
  --visitas-com-conversao $saida \
  --saida $saida_normalizacao \
  --normalize_technical $normalize_technical \
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
  --data-inicial $data_inicial \
  --data-final $data_final &&

echo '--------------------------'
echo 'Finishing Pipeline'
echo '--------------------------'
