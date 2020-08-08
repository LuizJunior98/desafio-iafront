import click

from desafio_iafront.jobs.escala_pedidos.preprocessing import Preprocessing

from desafio_iafront.jobs.common import prepare_dataframe


@click.command()
@click.option('--visitas-com-conversao', type=click.Path(exists=True))
@click.option('--saida', type=click.Path(exists=False, dir_okay=True, file_okay=False))
@click.option('--data-inicial', type=click.DateTime(formats=["%d/%m/%Y"]))
@click.option('--data-final', type=click.DateTime(formats=["%d/%m/%Y"]))
@click.option('--departamentos', type=str, help="Departamentos separados por virgula")
def main(visitas_com_conversao, saida, data_inicial, data_final, departamentos):
    departamentos_lista = [departamento.strip() for departamento in departamentos.split(",")]

    result = prepare_dataframe(departamentos_lista, visitas_com_conversao, data_inicial, data_final)

    preprocessing = Preprocessing(result, saida)

    preprocessing.normalizer()
    preprocessing.standard_scale()
    preprocessing.min_max_scale()
    preprocessing.max_abs_scale()
    preprocessing.robust_scale()
    preprocessing.power_transformer()


if __name__ == '__main__':
    main()
