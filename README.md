###ont_dap
----------

ont_dap is a collection of bash scripts that (a) help install/ config tools commonly 
used to analyze Oxford Nanopore Technologies (ONT) sequencing device data; and (b) 
streamline the use of these tools for sequencing performance and alignment analysis.

DISCLAIMER: very much a work-in-progress. 

####Dependencies
----------------
    Mac or Linux OS    
    R >= 3.0.0 
    ggplot2
    Python >= 2.7, < 3.0
    pip
	samtools

References for installing these:  
	
    pip: 	https://pip.pypa.io/en/latest/installing.html  
	R: 		https://www.r-project.org/  
	Python:	https://www.python.org/downloads/  

The dependencies that will automatically be installed (if they are not already):
	 
    h5py >= 2.0.0  
	rpy2 >= 2.4.2  
	watchdog >= 0.8.3


####Install/ Setup
------------------

WARNING: this is not fully functional.

	$ git clone https://www.github.com/tmfarrell/ont_dap.git
	$ cd ont_dap
	$ source setup.sh   


####Usage
---------

These should work provided all the dependencies for poretools installed properly.   

(1) Run poretools to assess sequencing run performance: 

    $ ./run_poretools.sh -h 
    
(2) Align and compute alignment statistics: 
    
    $ ./run_alignment.sh -h 
    

#####Contact: 
Tim Farrell, tfarrell01@gmail.com
