from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("input.pdf")
writer = PdfWriter()
writer.append_pages_from_reader(reader)

# copy existing metadata (if any) and overwrite dates
meta = reader.metadata or {}
meta.update({
    '/CreationDate': "D:20250101120000Z",
    '/ModDate':     "D:20250101120000Z",
})

writer.add_metadata(meta)
with open("output.pdf", "wb") as f:
    writer.write(f)
