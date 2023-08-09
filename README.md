# google-photos-backup-utils
My personal toolkit for Google Photo Extraction.  

## FlattenFileStructure.py
Google Photos Takeout will zip all files in a complex file structure with metadata files scattering all over the place. This util recursively flattens file structure. It further handles file name duplication; it renames duplicated file to `<fileName>__<countOfDuplicates>.<fileExtension>`. Note that files with different extensions are not duplicates, and so they won't be renamed (this is to avoid metadata file conflicts with the picture itself.)

## ModifyExtensionReprocess.py
When overlaying datetime metadata to photos, I received a lot of errors like:
Error: Not a valid HEIC (looks more like a JPEG) - ./IMG_0944.HEIC
These can be fixed by changing the file extension to .JPEG, and the corresponding metadata file
to .JPEG.json.
These two files will need to be moved to a different directory to perform the re-overlay
so that we don't need to overlay the original directory all over again (which might contains a lot of photos).

## FileRenamingTool.py
Sometimes when you move files to another folder, there might be duplicate file names. This util simply appends __avoid_dup to the end of file name (before file extension).
It doesn't do any extra processing, just rename files.