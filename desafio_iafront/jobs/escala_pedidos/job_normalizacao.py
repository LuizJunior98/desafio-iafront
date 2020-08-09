import click

from desafio_iafront.jobs.escala_pedidos.preprocessing import Preprocessing

from desafio_iafront.jobs.common import prepare_dataframe


@click.command()
@click.option('--visitas-com-conversao', type=click.Path(exists=True))
@click.option('--saida', type=click.Path(exists=False, dir_okay=True, file_okay=False))
@click.option('--data-inicial', type=click.DateTime(formats=["%d/%m/%Y"]))
@click.option('--data-final', type=click.DateTime(formats=["%d/%m/%Y"]))
@click.option('--departamentos', type=str, help="Departamentos separados por virgula")
@click.option('--normalize_technical', type=str)
def main(visitas_com_conversao, saida, data_inicial, data_final, departamentos, normalize_technical: str):
    departamentos_lista = [departamento.strip() for departamento in departamentos.split(",")]

    result = prepare_dataframe(departamentos_lista, visitas_com_conversao, data_inicial, data_final)

    preprocessing = Preprocessing(result, saida)

    if normalize_technical.lower().strip() == 'normalizer':
        preprocessing.normalizer()
    elif normalize_technical.lower().strip() == 'standard_scale':
        preprocessing.standard_scale()
    elif normalize_technical.lower().strip() == 'min_max_scale':
        preprocessing.min_max_scale()
    elif normalize_technical.lower().strip() == 'max_abs_scale':
        preprocessing.max_abs_scale()
    elif normalize_technical.lower().strip() == 'robust_scale':
        preprocessing.robust_scale()
    elif normalize_technical.lower().strip() == 'power_transformer':
        preprocessing.power_transformer()
    else:
        preprocessing.normalizer()
        preprocessing.standard_scale()
        preprocessing.min_max_scale()
        preprocessing.max_abs_scale()
        preprocessing.robust_scale()
        preprocessing.power_transformer()


if __name__ == '__main__':
    main()
