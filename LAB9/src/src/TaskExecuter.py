import dataManager as dm
import OctaveSolver as ocsol
import Ploater as pltr

# class which provide all task execution
class TaskExecuter:
    # arguments:
    #   - filePR1 : path to csv with 1st Photon Reciver data
    #   - filePR2 : path to csv with 2nd Photon Reciver data
    #   - fileLR1 : path to txt with linear regrestion of 1st Photon Reciver data
    #   - fileLR2 : path to csv with linear regrestion of 2nd Photon Reciver data
    #   - startCSVOffset : first strings offset in csv files
    #   - eps : epsilon in interval
    #   - isShow : are plots must be showen
    #   - isShow : are plots must be saved
    #   - savePath : path where save plots
    def __init__(self, filePR1 : str, filePR2 : str, fileLR1 : str, fileLR2 : str, startCSVOffset : int, eps : float, isShow : bool, isSave : bool, savePath : str):
        self.offset = startCSVOffset
        self.filePR1 = filePR1
        self.filePR2 = filePR2
        self.fileLR1 = fileLR1
        self.fileLR2 = fileLR2
        self.eps = eps
        self.isShow = isShow
        self.isSave = isSave
        self.savePath = savePath
        return

    def loadData(self):
        # load data
        dataManager= dm.DataManager()
        self.data = dataManager.loadData(self.filePR1, self.offset)
        self.etalonData = dataManager.loadData(self.filePR2, self.offset)
        return

    def findOctaves(self):
        octaveSolver = ocsol.LinearSolutionManager()
        self.tau, self.w = octaveSolver.openLinearSolution(self.fileLR1)
        self.etalonTau, self.etalonW = octaveSolver.openLinearSolution(self.fileLR2)
        return

    def plotGraphs(self):
        plotter = pltr.Plotter(self.isShow, self.isSave, self.savePath)

        plotter.plotInputDatas(self.data, self.etalonData)
        plotter.plotIntervals(self.data, self.etalonData, self.eps)
        plotter.plotLinearRegression(self.data, self.tau, self.w, self.etalonData, self.etalonTau, self.etalonW, self.eps)
        plotter.plotHystW(self.w, self.etalonW)
        plotter.plotFixedIntervals(self.data, self.tau, self.w, self.etalonData, self.etalonTau, self.etalonW, self.eps)
        plotter.plotFixedHyst(self.data, self.tau, self.w, self.etalonData, self.etalonTau, self.etalonW, self.eps)
        optimal_x = plotter.plotJacard(self.data, self.tau, self.w, self.etalonData, self.etalonTau, self.etalonW, self.eps)
        plotter.plotJacardHyst(self.data, self.tau, self.w, self.etalonData, self.etalonTau, self.etalonW, self.eps, optimal_x)
        return

    def execute(self):
        # load data from csv
        self.loadData()
        # find octaves
        self.findOctaves()
        # plot graphs
        self.plotGraphs()
        return
