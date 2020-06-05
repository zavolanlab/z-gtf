#!/usr/bin/env python

import os

def test_gtf2bed12_path(script_runner):
    ret = script_runner.run('gtf2bed12', '--help')
    assert ret.success

def test_gtf2bed12_plus_strand(script_runner):
    
    gtf = "test_data/test.gtf"
    out = "test_data/out.bed"
    
    script_runner.run('gtf2bed12',
                      '--gtf', gtf,
                      '--bed12', out,
                      '--transcript_type', 'processed_transcript')
    
    w = open(out, "r")
    lines = w.readline()
    w.close()
    
    assert lines == "\t".join(["1-10000-20000", 
                              "1869", 
                              "4410", 
                              "ENST00000456328", 
                              "1", 
                              "+", 
                              "1869", 
                              "4410",
                              "0",
                              "3",
                              "359,109,1189,",
                              "0,744,1352," + os.linesep
                            ])
    
    os.remove(out)

def test_gtf2bed12_minus_strand(script_runner):
    
    gtf = "test_data/test.gtf"
    out = "test_data/out.bed"
    
    script_runner.run('gtf2bed12',
                      '--gtf', gtf,
                      '--bed12', out,
                      '--transcript_type', 'unprocessed_pseudogene')
    
    w = open(out, "r")
    lines = w.readline()
    w.close()
    
    assert lines == "\t".join(["1-10000-20000", 
                              "4404", 
                              "8367", 
                              "ENST00000488147", 
                              "1", 
                              "-", 
                              "4404", 
                              "8367",
                              "0",
                              "9",
                              "98,34,152,159,198,136,137,147,99,",
                              "0,601,1392,2203,2454,2829,3202,3511,3864," + os.linesep
                            ])
    
    os.remove(out)