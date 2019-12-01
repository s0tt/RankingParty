import matplotlib
matplotlib.use('Qt5Agg')   # generate postscript output by default
from Plotter import Plotter
from matplotlib import animation, pyplot
from config import plotterConfig

def main():
    RankingPlotter = Plotter()
    fig, axis = RankingPlotter.plotFigure()

    ## position figure and set size
    mngr = pyplot.get_current_fig_manager()
    # to put it into the upper left corner for example:
    mngr.window.showMaximized()
    #mngr.window.setGeometry(0,0,1920, 1080)


    bars = RankingPlotter.plotHBar(axis)
    RankingPlotter.readDB()
    anim = animation.FuncAnimation(fig, RankingPlotter.animateHBarFunc, fargs=(bars,), interval=plotterConfig["animIntervall"], repeat=False, blit=False) ##interval in ms
    pyplot.show()


if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function