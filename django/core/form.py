from django import forms

MAX_VIDEO_CHUNK_SIZE = 1 * 1024 * 1024  # 1MB


class VideoChunkUploadForm(forms.Form):
    chunk = forms.FileField(required=True)  # O arquivo chunk
    # Índice do chunk (deve ser >= 0)
    chunkIndex = forms.IntegerField(min_value=0, required=True)

    def clean_chunk(self):
        chunk = self.cleaned_data.get('chunk')

        if chunk.size > MAX_VIDEO_CHUNK_SIZE:
            raise forms.ValidationError(
                'O chunk é maior que 1MB')

        return chunk


class VideoChunkFinishUploadForm(forms.Form):
    fileName = forms.CharField(
        max_length=255, required=True)  # Nome do arquivo

    # Total de chunks (deve ser >=1)
    totalChunks = forms.IntegerField(min_value=1, required=True)
