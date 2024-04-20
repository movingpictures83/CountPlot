import matplotlib.pyplot as plt
import seaborn as sns
import pandas

import PyPluMA
import PyIO

class CountPlotPlugin:
 def input(self, inputfile):
  self.parameters = PyIO.readParameters(inputfile)
  self.df = pandas.read_csv(PyPluMA.prefix()+"/"+self.parameters["csvfile"])
 def run(self):
  self.df.drop_duplicates(inplace=True)
  sns.countplot(x=self.parameters["x"],data=self.df, palette=self.parameters["palette"])
 def output(self, outputfile):
  plt.savefig(outputfile)
