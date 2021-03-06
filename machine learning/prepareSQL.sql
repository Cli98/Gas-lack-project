  Select * 
  from	[gaspro].[dbo].[PLUTO_MN_GeoClient_up]

  Where geo_code in (

  SELECT [gaspro].[dbo].[PLUTO_MN_GeoClient_up].geo_code
  FROM [gaspro].[dbo].[PLUTO_MN_GeoClient_up]
  INNER JOIN [gaspro].[dbo].[BOPA_MN_O_Address_GEO_up] ON 
  [gaspro].[dbo].[BOPA_MN_O_Address_GEO_up].geo_code = [gaspro].[dbo].[PLUTO_MN_GeoClient_up].geo_code)

  Select * 
  from	[gaspro].[dbo].[PLUTO_MN_GeoClient_up]

  Where geo_code in (

  SELECT [gaspro].[dbo].[PLUTO_MN_GeoClient_up].geo_code
  FROM [gaspro].[dbo].[PLUTO_MN_GeoClient_up]
  INNER JOIN [gaspro].[dbo].[BOPA_MN_N_Address_GEO_up] ON 
  [gaspro].[dbo].[BOPA_MN_N_Address_GEO_up].geo_code = [gaspro].[dbo].[PLUTO_MN_GeoClient_up].geo_code)

  SELECT COUNT(*)
  FROM [gaspro].[dbo].[BOPA_MN_N_Address_GEO_up]

  SELECT COUNT(*)
  FROM [gaspro].[dbo].[BOPA_MN_O_Address_GEO_up]
