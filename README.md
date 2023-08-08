# google-photos-backup-utils
My personal toolkit for Google Photo Extraction.  

## FlattenFileStructure.py
Google Photos Takeout will zip all files in a complex file structure with metadata files scattering all over the place. This util recursively flattens file structure. It further handles file name duplication; it renames duplicated file to <fileName>__<countOfDuplicates>.<fileExtension>. Note that files with different extensions are not duplicates, and so they won't be renamed (this is to avoid metadata file conflicts with the picture itself.)
