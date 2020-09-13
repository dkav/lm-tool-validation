# Climate Linkage Mapper

import arcpy


class ToolValidator(object):
    """Class for validating a tool's parameter values and controlling
    the behavior of the tool's dialog."""

    def __init__(self):
        """Setup arcpy and the list of tool parameters."""
        self.params = arcpy.GetParameterInfo()

    def initializeParameters(self):
        """Refine the properties of a tool's parameters.
        This method is called when the tool is opened."""

    def updateParameters(self):
        """Modify the values and properties of parameters before internal
        validation is performed. This method is called whenever a parameter
        has been changed."""
        # Disable optional parameters when not required
        if self.params[10].value:
            self.params[11].enabled = True
            self.params[12].enabled = True
            self.params[13].enabled = True
        else:
            self.params[11].enabled = False
            self.params[12].enabled = False
            self.params[13].enabled = False

    def updateMessages(self):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""
        # Project dir validation
        if not self.params[0].hasError() and self.params[0].altered:
            if (len(str(self.params[0].value)) > 100 or
                    set("# ").intersection(str(self.params[0].value))):
                self.params[0].setErrorMessage("Project directory must be less"
                                               " than 100 characters in length"
                                               " and must not contain spaces.")

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True
