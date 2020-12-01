obj_files = getFiles "E://桌面//新建文件夹//111//*.obj"  
for f in obj_files do   
(  
    if ( doesfileexist f ) do  
        importFile f #noPrompt using:Wavefront_Object
    for geo in geometry   
        where (matchPattern geo.name pattern:"3D_Object*") do  
    (  
            --geo.name = (f as string)   
            pathaa = filterString (f as string) "//"  
            geo.name = pathaa[pathaa.count]  
    )  
)  