"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import glob
import os

import matplotlib.pyplot as plt
import pandas as pd

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    def plot_data(df, graph_path):

        def series_properties():
            # [color, zorder, linewidth]
            return {
                "Television": ["dimgray", 1, 2],
                "Newspaper": ["grey", 1, 2],
                "Internet": ["tab:blue", 2, 3],
                "Radio": ["lightgrey", 1, 2],
            }

        def set_markers(df, col):

            for i in [0, -1]:
                plt.scatter(
                    x=df.index[i],
                    y=df[col].iloc[i],
                    color=series_properties()[col][0],
                )

        def set_labels(df, col):

            for i in [0, -1]:
                offset = 0.2 if i == 0 else -0.2
                horizontal_aligment = "right" if i == 0 else "left"
                text_value = (
                    f"{col} {str(df[col][df.index[i]])} %"
                    if i == 0
                    else f"{str(df[col][df.index[i]])} %"
                )
                plt.text(
                    df.index[i] - offset,
                    df[col][df.index[i]],
                    text_value,
                    ha=horizontal_aligment,
                    va="center",
                    color=series_properties()[col][0],
                )

        def set_xticks(df):

            plt.xticks(
                ticks=df.index,
                labels=df.index,
                ha="center",
            )

        def create_graph(df):

            for col in df.columns:
                # Series de tiempo
                plt.plot(
                    df[col],
                    label=col,
                    color=series_properties()[col][0],
                    zorder=series_properties()[col][1],
                    linewidth=series_properties()[col][2],
                )
                # Marcadores
                set_markers(df, col)
                # Etiquetas
                set_labels(df, col)
                # Xticks
                set_xticks(df)

        def beautify_graph():

            plt.title("How people get theri news", fontsize=16)
            plt.gca().spines["top"].set_visible(False)
            plt.gca().spines["left"].set_visible(False)
            plt.gca().spines["right"].set_visible(False)
            plt.gca().axes.get_yaxis().set_visible(False)
            plt.tight_layout()
            plt.annotate(
                "An increasing proportion cite the internet as their primary news source",
                xy=(0.5, 1),
                xycoords="axes fraction",
                xytext=(0.5, 0.97),
                textcoords="axes fraction",
                horizontalalignment="center",
                fontsize=7,
            )

        def save_graph(graph_path):
            graph_dir = os.path.dirname(graph_path)
            if os.path.exists(graph_dir):
                for file in glob.glob(f"{graph_dir}/*"):
                    os.remove(file)
                os.rmdir(graph_dir)
            os.makedirs(graph_dir)
            plt.savefig(graph_path)

        create_graph(df)
        beautify_graph()
        save_graph(graph_path)

    df = pd.read_csv("files/input/news.csv", index_col=0)
    plot_data(df, "files/plots/news.png")

    return "Grafico generado"


if __name__ == "__main__":
    print(pregunta_01())