import sys, csv
from src.msds510.avenger import *

# if the avenger utility is supposed to be imported here, how do I do that? Which utility?
# Can use Avenger, or * since the entire class is one object
# generateReport('C:\\Users\\jfrip\\OneDrive\\Data Science Workspaces\\School\\FRIPP_Final_Project\\data\\
# processed\\dc-wikia-data-processed.csv','C:\\Users\\jfrip\\
# OneDrive\\Data Science Workspaces\\School\\FRIPP_Final_Project\\src\\reports\\dc-report.md')

def main():
    """interprets command line request
    Args:
        argv: an array with input and output files

    Returns:
        no return. Executed generateReport with
        collected file names.
    """
    if len(sys.argv) != 3:
        print("this report generator takes two parameters, "
              "an input file and an output file")
    else:
        print("input file: " + sys.argv[1])
        print("output file: " + sys.argv[2])
        generateReport(sys.argv[1], sys.argv[2])


def generateReport(infile, outfile):
    """
    reads an infile, sorts the content, and
       sends the sorted records and an outfile
       destination to printMarkdown to print
    Args:
        infile: a file location to read data from
        outfile: a destination file location
    Result:
        executes the printMarkdown function with
        sorted records and an outfile to write
        the results to.
    """

    file = []
    with open(infile, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        file = list(reader)

    sortedRecords = sorted(file,
                           key=lambda k: int(k['appearances']),
                           reverse=True)[:10]

    dc-character = dc-character()
    dc-character.to_markdown(sortedRecords, outfile)

if __name__ == '__main__':
    main()
