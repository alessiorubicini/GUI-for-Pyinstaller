from tkinter.filedialog import *


# Controller
class Controller(object):
    
    # Constructor
    def __init__(self, view):
        global extraFiles
        
        self.view = view
        extraFiles = []

    
    # Python file selection
    def askFilePy(self):
        global pyFile

        # Asl for file name
        pyFile = askopenfilename(initialdir="/", title="Select .py file", filetypes=(("Python Files (.py)", "*.py"), ("all files", "*.*")))

        # Check if user close file dialog window 
        if not pyFile:
            view.pathError('python file.')
            return

        # Adjust spaces
        pyFile = pyFile.replace(" ", "\\ ")
        
        # DEBUG
        print("SCRIPT PATH: ", pyFile)


    
    # Extra files selection
    def askExtraFiles(self):
        global extraFiles

        # Ask for extra files
        extraFiles = askopenfilenames(initialdir="/", title="Select extra files")

        # Check if user close file dialog window 
        if not extraFiles:
            view.pathError('extra file.')
            return

        # Iterate ovre list of files specified by the user
        for path in extraFiles:
            path = str(path)
            path = path.replace(" ", "\\ ")
            path = path.strip("'")

        print("FILE EXTRA: ", extraFiles)


    # Output directory selection
    def askOutputDirectory(self):
        global outputDirectory
        
        outputDirectory = askdirectory()

        # Check if user specified the output directory
        if not outputDirectory:
            view.pathError('output directory.')
            return

        outputDirectory = outputDirectory.replace(" ", "\\ ")

        outputDirectory = '--distpath ' + outputDirectory

    
    
    # Executable icon selection
    def askExecutableIcon(self):
        global icon

        # Ask for executable icon file (.ico)
        icon = askopenfilename(initialdir="/", title="Select .ico file", filetypes=(("Icon Files (.ico)", "*.ico"), ("all files", "*.*")))

        # Check if user close file dialog window 
        if not icon:
            view.pathError('icon path.')
            return

        # Adjust spaces
        icon = icon.replace(" ", "\\ ")

        icon = '--icon=' + icon


    
    # File conversion
    def convertiFile(self, exportMode, softwareMode):
        global pyFile, outputDirectory, extraFiles, icon

        # Parsing from StringVar to String
        exportMode = str(exportMode.get())
        softwareMode = str(softwareMode.get())

        # Check if python file has been specified
        try:
            print("Python file: " + pyFile)
        except:
            view.notDeclared('Python file')
            return
        

        # Check if output directory has been specified
        try:
            print("Output directory: " + outputDirectory)
        except:
            view.notDeclared('Output directory')
            return


        # If the user have specified extra files
        if extraFiles:
            
            for file in extraFiles:
                extraFilesString = extraFilesString + ' ' + '--add-data "' + file + ':."' + ''
            
            print(extraFilesString)

            # Build the final command
            command = 'pyinstaller' + ' ' + extraFilesString + ' '
            command = command + pyFile + ' ' + exportMode + ' ' + softwareMode + ' ' + outputDirectory

        else:
            # Build the final command without extra files
            command = 'pyinstaller' + ' ' + pyFile + ' ' + exportMode + ' ' + softwareMode + ' ' + outputDirectory

        print("Final command:  " + command)

        
        # Try to run the command
        try:
            os.system(command)

            messagebox.showwarning("Great!", "Conversion completed successfully!")
        
        except:
            view.conversionError()
            return
        
        