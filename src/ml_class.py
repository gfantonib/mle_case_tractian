import pandas as pd

class mlModel:

	def __init__(self):
		self.sensors_groups = None
		self.df_sensors_groups_means = None
		self.df_sensors_groups_stds = None
		self.df_result = None

	def train(self, df:pd.DataFrame):
		sensors_groups = df.groupby("sensorId")
		self.df_sensors_groups_means = sensors_groups.mean()
		self.df_sensors_groups_stds = sensors_groups.std()

	def predict(self, discriminator: float):
		self.df_result = discriminator >= self.df_sensors_groups_means + 2*self.df_sensors_groups_stds

	def get_df_result(self):
		return self.df_result


	