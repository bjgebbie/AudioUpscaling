class upscaler:
    def __init__(self, wave_file, interpolation):
        self.wave_file = wave_file
        self.interpolation = interpolation
        
        if interpolation == 'cs':
            # run cubic spline and write to a file
            pass
