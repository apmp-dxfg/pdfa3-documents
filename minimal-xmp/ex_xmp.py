from pypdf import PdfReader

meta = PdfReader("ex_xmp.pdf").xmp_metadata 

print( meta.dc_title )
print( meta.dc_creator )
print( meta.dc_date )
print( meta.dc_publisher )
