/****** Script for SelectTopNRows command from SSMS  ******/
SELECT *
  FROM [gaspro].[dbo].[BOPA_MN_O_Address_final]
  INNER JOIN [gaspro].[dbo].[PLUTO_final] ON 
  [gaspro].[dbo].[BOPA_MN_O_Address_final].Latitude = [gaspro].[dbo].[PLUTO_final].Latitude
  AND
  [gaspro].[dbo].[BOPA_MN_O_Address_final].Longitude = [gaspro].[dbo].[PLUTO_final].Longitude

 SELECT *
  FROM [gaspro].[dbo].[BOPA_MN_N_Address_final]
  INNER JOIN [gaspro].[dbo].[PLUTO_final] ON 
  [gaspro].[dbo].[BOPA_MN_N_Address_final].Latitude = [gaspro].[dbo].[PLUTO_final].Latitude
  AND
  [gaspro].[dbo].[BOPA_MN_N_Address_final].Longitude = [gaspro].[dbo].[PLUTO_final].Longitude

  SELECT *
  FROM [gaspro].[dbo].[PLUTO_final]
  INNER JOIN [gaspro].[dbo].[BOPA_MN_N_Address_final] ON 
  [gaspro].[dbo].[BOPA_MN_N_Address_final].Latitude = [gaspro].[dbo].[PLUTO_final].Latitude
  AND
  [gaspro].[dbo].[BOPA_MN_N_Address_final].Longitude = [gaspro].[dbo].[PLUTO_final].Longitude

  SELECT DISTINCT
	   ABS(CAST([gaspro].[dbo].[BOPA_MN_O_Address_final].[Latitude] AS float)-CAST([gaspro].[dbo].[PLUTO_final].[Latitude] AS float))As Lat
      ,ABS(CAST([gaspro].[dbo].[BOPA_MN_O_Address_final].[Longitude]AS float)-CAST([gaspro].[dbo].[PLUTO_final].[Longitude] AS float))As Lon
	  ,[gaspro].[dbo].[BOPA_MN_O_Address_final].[GI_BA_S_CP]
      ,[GI_BA_S_STREET]
      ,[GI_BA_S_ARTERY]
      ,[GI_BA_S_HOUSE_NO]
	  ,[gaspro].[dbo].[PLUTO_final].[Address]
	  ,[gaspro].[dbo].[BOPA_MN_O_Address_final].Latitude
	  ,[gaspro].[dbo].[BOPA_MN_O_Address_final].Longitude

  FROM [gaspro].[dbo].[BOPA_MN_O_Address_final],[gaspro].[dbo].[PLUTO_final]

WHERE ABS(CAST([gaspro].[dbo].[BOPA_MN_O_Address_final].[Latitude] AS float)-CAST([gaspro].[dbo].[PLUTO_final].[Latitude] AS float))<0.0005 AND 
	  ABS(CAST([gaspro].[dbo].[BOPA_MN_O_Address_final].[Longitude]AS float)-CAST([gaspro].[dbo].[PLUTO_final].[Longitude] AS float))<0.0005


 SELECT DISTINCT
	   ABS(CAST([gaspro].[dbo].[BOPA_MN_O_Address_final].[Latitude] AS float)-CAST([gaspro].[dbo].[PLUTO_final].[Latitude] AS float))
      ,ABS(CAST([gaspro].[dbo].[BOPA_MN_O_Address_final].[Longitude]AS float)-CAST([gaspro].[dbo].[PLUTO_final].[Longitude] AS float))
	 

  FROM [gaspro].[dbo].[BOPA_MN_O_Address_final],[gaspro].[dbo].[PLUTO_final]

WHERE ABS(CAST([gaspro].[dbo].[BOPA_MN_O_Address_final].[Latitude] AS float)-CAST([gaspro].[dbo].[PLUTO_final].[Latitude] AS float))<0.0005 AND 
	  ABS(CAST([gaspro].[dbo].[BOPA_MN_O_Address_final].[Longitude]AS float)-CAST([gaspro].[dbo].[PLUTO_final].[Longitude] AS float))<0.0005
