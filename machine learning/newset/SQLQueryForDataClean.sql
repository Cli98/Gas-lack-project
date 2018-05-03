  Select * 
  from	[gaspro].[dbo].[PLUTO_MN_GeoClientf]

  Where ([gaspro].[dbo].[PLUTO_MN_GeoClientf].[corx] NOT in (

  SELECT [gaspro].[dbo].[PLUTO_MN_GeoClientf].[corx]
      
  FROM [gaspro].[dbo].[PLUTO_MN_GeoClientf]
  INNER JOIN [gaspro].[dbo].[BOPA_MN_O_Address_GEO_SplitGEO] ON 
  [gaspro].[dbo].[BOPA_MN_O_Address_GEO_SplitGEO].[Latitude] = [gaspro].[dbo].[PLUTO_MN_GeoClientf].[corx]
  And
  [gaspro].[dbo].[BOPA_MN_O_Address_GEO_SplitGEO].[Longitude] = [gaspro].[dbo].[PLUTO_MN_GeoClientf].[cory]
  )
  AND
  [gaspro].[dbo].[PLUTO_MN_GeoClientf].[corx] > '0')
