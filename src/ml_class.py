import pandas as pd

class mlModel:

	def __init__(self):
		self.df = None
		self.sensors_groups = None
		self.df_sensors_groups_means = None
		self.df_sensors_groups_stds = None
		self.df_result = None

	def prepare_data(self, df: pd.DataFrame):
		self.df = df
		df_light = self.df.drop(["_id", "createdAt", "params.duration", "params.sampRate", "params.timeStart", "temp"], axis=1)
		self.sensors_groups = df_light.groupby("sensorId")

	def train(self):
		self.df_sensors_groups_means = self.sensors_groups.mean()
		self.df_sensors_groups_stds = self.sensors_groups.std()

	def predict(self, discriminator: float):
		self.df_result = discriminator >= self.df_sensors_groups_means + 2*self.df_sensors_groups_stds

	def get_df_result(self):
		return self.df_result


	