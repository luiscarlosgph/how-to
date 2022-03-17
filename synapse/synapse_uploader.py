"""
@brief  Script to upload files or folders into a synapse project.
@author Luis Carlos Garcia Peraza Herrera (luiscarlos.gph@gmail.com).
@date   16 Sep 2020.
"""
import argparse
import os
import sys
import synapseclient


# Command line options
helpmsg = {
    '--username':   'Synapse username',
    '--password':   'Synapse password',
    '--input-path': 'Path to the file/directory \
                     to be uploaded.',
    '--parent-id':  'Synapse ID of the project or \
                     directory where data will be \
                     uploaded to.',
}


def parse_cmdline():
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--username', required=True, 
                        help=helpmsg['--username'])
    parser.add_argument('--password', required=True, 
                        help=helpmsg['--password'])
    parser.add_argument('--input-path', required=True, 
                        help=helpmsg['--input-path'])
    parser.add_argument('--parent-id', required=True, 
                        help=helpmsg['--parent-id'])
    args = parser.parse_args()
    return args

def validate_args(args): 
    if not os.path.isdir(args.input_path) \
            and not os.path.isfile(args.input_path):
        raise ValueError('The input path does not exist.')


def upload(path, parent, syn, hidden=False):
    """
    @brief Upload a file or folder to the Synapse 
           repository.
    @param[in]  path       Path to the local file/dir 
                           to upload.
    @param[in]  parent     Synapse data structure that
                           represents a project or a
                           remote folder.
    @param[in]  syn        Synapse client.
    @param[in]  hidden     Flag to upload hidden files.
                           False by default.
    @returns nothing.
    """
    # Upload file
    if os.path.isfile(path):
        fname = os.path.basename(path)
        if hidden or not fname.startswith('.'):
            data = synapseclient.File(path, parent)
            syn.store(data)

    # Upload a directory
    elif os.path.isdir(path):
        fname = os.path.basename(path)
        folder = synapseclient.Folder(fname, parent)
        folder = syn.store(folder)
        for f in os.listdir(path):
            upload(os.path.join(path, f), folder, syn, 
                   hidden)
    else:
        print('[WARN] The path ' + path + ' does not ' \
              + 'contain a file or a folder. Ignored.')


def main():
    # Read command line arguments
    args = parse_cmdline()
    
    # Connect to Synapse
    syn = synapseclient.Synapse()
    syn.login(args.username, args.password)

    # Upload files or folders to Synapse
    upload(args.input_path, syn.get(args.parent_id), syn)


if __name__ == '__main__':
    main()
