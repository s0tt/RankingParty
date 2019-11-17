from Plotter import Plotter
from matplotlib import animation, pyplot
from config import plotterConfig

def main():
    RankingPlotter = Plotter()
    fig, axis = RankingPlotter.plotFigure()
    bars = RankingPlotter.plotHBar(axis)
    anim = animation.FuncAnimation(fig, RankingPlotter.animateHBarFunc, fargs=(bars,), interval=plotterConfig["animIntervall"], repeat=False, blit=False) ##interval in ms
    pyplot.show()


if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function