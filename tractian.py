import pandas as pd

class Tractian:

	def __init__(self, df: pd.DataFrame):
		self.df = df
		self.sensor_groups = None
		self.sensor_groups_means = None
		self.sensor_groups_stds = None
		self.result_df = None

	def clean_data(self):
		df_light = self.df.drop(["_id", "createdAt", "params.duration", "params.sampRate", "params.timeStart", "temp"], axis=1)
		self.sensor_groups = df_light.groupby("sensorId")

	def train(self):
		self.sensor_groups_means = self.sensor_groups.mean()
		self.sensor_groups_stds = self.sensor_groups.std()

	def predict(self, discriminator: float):
		self.result_df = discriminator >= self.sensor_groups_means + 2*self.sensor_groups_stds

	def get_result_df(self):
		return self.result_df


	