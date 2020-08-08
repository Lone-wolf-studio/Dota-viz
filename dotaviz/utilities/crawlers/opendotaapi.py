

class OpenDotaApiCrawler:
	opendota_url =  "https://api.opendota.com/api/"

	@classmethod
	def _get_players_list(cls):
		all_players_list_url = cls._get_api_parameter_url(parameter)
		return all_players_list_url

	@classmethod
	def _get_matches_list(cls):
		all_matches_list_url = cls._get_api_parameter_url(parameter)
		return all_matches_list_url

	@classmethod
	def _get_heros_list(cls):
		all_heros_list_url = cls._get_api_parameter_url(parameter)
		return all_heros_list_url

	@classmethod
	def _get_proplayers_list(cls):
		all_proplayers_list_url = cls._get_api_parameter_url(parameter)
		return all_proplayers_list_url

	@classmethod
	def _get_promatches_list(cls):
		all_promatches_list_url = cls._get_api_parameter_url(parameter)				
		return all_promatches_list_url

	@classmethod
	def _get_all_teams_list_url(cls): 
		all_teams_list_url = cls._get_all_teams_list_url(parameter)
		return all_teams_list_url	
	
	@classmethod
	def _get_api_parameter_url(cls, parameter):
		url_parameter = cls.opendota_url + '/' + parameter
		return url_parameter
		
	
